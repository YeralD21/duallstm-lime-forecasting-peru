"""Ridge y ElasticNet tabulares (37 predictores de XGB-37; X estandarizado en train; y en toneladas).

Dos implementaciones de ElasticNet:
  - sklearn (la que usa el backtesting).
  - port exacto del descenso coordenado de v3 (run_robustez.mjs:71-75), solo para diagnosticar la reproduccion.
Ambas minimizan 1/(2n)||y - b - Xw||^2 + a*l1*||w||_1 + a*(1-l1)/2*||w||^2 con X estandarizado (desviacion poblacional).
"""
from __future__ import annotations

import numpy as np
from sklearn.linear_model import ElasticNet, Ridge


class EstandarizadorV3:
    """scaleFit de v3 (run_robustez.mjs:59-62): media y desviacion poblacional; sd<=1e-12 -> 1."""

    def ajustar(self, X: np.ndarray) -> "EstandarizadorV3":
        self.mu = X.mean(axis=0)
        sd = np.sqrt(((X - self.mu) ** 2).mean(axis=0))
        self.sd = np.where(sd > 1e-12, sd, 1.0)
        return self

    def transformar(self, X: np.ndarray) -> np.ndarray:
        return (X - self.mu) / self.sd


def elasticnet_sklearn(X: np.ndarray, y: np.ndarray, alpha: float, l1: float) -> tuple[float, np.ndarray]:
    m = ElasticNet(alpha=alpha, l1_ratio=l1, fit_intercept=True, max_iter=100_000, tol=1e-10, selection="cyclic")
    m.fit(X, y)
    return float(m.intercept_), m.coef_.copy()


def elasticnet_v3(X: np.ndarray, y: np.ndarray, alpha: float, l1: float) -> tuple[float, np.ndarray]:
    """Port literal de elasticFit de v3: 4000 iteraciones maximas, parada si sum|cambio| < 1e-7."""
    n, p = X.shape
    w = np.zeros(p)
    b = float(np.mean(y))
    for _ in range(4000):
        viejo = np.concatenate([[b], w])
        b = float(np.mean(y - X @ w))
        for j in range(p):
            r = y - b - X @ w + X[:, j] * w[j]
            rho = float(X[:, j] @ r)
            z, g = rho / n, alpha * l1
            soft = z - g if z > g else (z + g if z < -g else 0.0)
            w[j] = soft / (1 + alpha * (1 - l1))
        if float(np.abs(viejo - np.concatenate([[b], w])).sum()) < 1e-7:
            break
    return b, w


def ridge_sklearn(X: np.ndarray, y: np.ndarray, alpha: float) -> tuple[float, np.ndarray]:
    """sklearn Ridge: ||y - b - Xw||^2 + alpha||w||^2, intercepto sin penalizar (igual a ridgeFit de v3)."""
    m = Ridge(alpha=alpha, fit_intercept=True, solver="auto")
    m.fit(X, y)
    return float(m.intercept_), m.coef_.copy()


def predecir(b: float, w: np.ndarray, X: np.ndarray) -> np.ndarray:
    return b + X @ w


def seleccionar_por_validacion(modelo: str, Xtr: np.ndarray, ytr: np.ndarray, Xva: np.ndarray, yva: np.ndarray,
                               alphas, l1s) -> tuple[dict, list[dict]]:
    """D-BR2 (DA4 revisada): cada candidato se ajusta en train; se elige el menor MAE de validacion en toneladas.

    Recorre la rejilla en su orden (alpha creciente; en ElasticNet l1 creciente dentro de cada alpha) y solo
    reemplaza al mejor con una mejora estricta: un empate queda en el primero de la rejilla.
    X ya estandarizado con el train de la ventana.
    """
    if list(alphas) != sorted(alphas) or list(l1s) != sorted(l1s):
        raise ValueError("La rejilla debe estar en orden creciente para que el desempate sea el preregistrado.")
    tabla, mejor = [], None
    combos = [(a, None) for a in alphas] if modelo == "Ridge" else [(a, l1) for a in alphas for l1 in l1s]
    for orden, (a, l1) in enumerate(combos):
        b, w = ridge_sklearn(Xtr, ytr, a) if modelo == "Ridge" else elasticnet_sklearn(Xtr, ytr, a, l1)
        mae_val = float(np.mean(np.abs(yva - predecir(b, w, Xva))))
        fila = {"orden_rejilla": orden, "alpha": a, "l1_ratio": l1, "MAE_val": mae_val}
        tabla.append(fila)
        if mejor is None or mae_val < mejor["MAE_val"]:
            mejor = {**fila, "b": b, "w": w}
    return mejor, tabla

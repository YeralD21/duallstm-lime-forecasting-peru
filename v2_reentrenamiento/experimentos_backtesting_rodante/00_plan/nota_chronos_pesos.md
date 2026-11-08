# Chronos-Bolt-tiny: identificación y cómo obtener los pesos en otro equipo

## Identificación (verificada en este equipo el 2026-10-25)

| Campo | Valor |
|---|---|
| Modelo | `amazon/chronos-bolt-tiny` (Hugging Face Hub) |
| Revisión (commit del snapshot) | `a0e552de83495b5c28c14c71c374f3e33280b340` (es la que apunta `refs/main` en la caché local) |
| `model.safetensors` | 34 622 352 bytes; SHA-256 `75068728d376d2bec670379eeef4bfb4d24c0cfe24d957451f8d19b447030a32` |
| `config.json` | 1 120 bytes; SHA-256 `278f0086733031635fb1c861cb01c1bad6477420c7fcb19381a2993e335785e0` |
| Paquete de inferencia | `chronos-forecasting 2.3.2` vendorizado en `v4_benchmark_moderno/vendor/` (junto con `einops 0.8.2`); 42 archivos `.py` con hash en `01_configuracion/hashes_congelados.json` |
| Dependencias del venv | torch 2.11.0+cpu, transformers 5.5.4, safetensors 0.7.0, huggingface_hub 1.10.2 |

## Obtener los pesos en otro equipo

Este paso requiere internet **una sola vez**. El experimento se ejecuta siempre sin conexión.

1. Use el mismo venv (Python 3.11) y no instale `chronos-forecasting`: el experimento usa la copia de `v4_benchmark_moderno/vendor/` (incluida en el commit).
2. Descargue la revisión fijada a la caché estándar de Hugging Face:

   ```powershell
   venv\Scripts\python.exe -c "from huggingface_hub import snapshot_download; print(snapshot_download('amazon/chronos-bolt-tiny', revision='a0e552de83495b5c28c14c71c374f3e33280b340'))"
   ```

   Los archivos quedan en `%USERPROFILE%\.cache\huggingface\hub\models--amazon--chronos-bolt-tiny\snapshots\a0e552de83495b5c28c14c71c374f3e33280b340\`. Si se usa `HF_HOME`, la ruta cambia y hay que ajustar `chronos_cache` en `01_configuracion/rutas_datos.json`.

3. Si `refs/main` no apunta a esa revisión, porque el repositorio del modelo recibió commits posteriores, escriba `a0e552de83495b5c28c14c71c374f3e33280b340` en `...\models--amazon--chronos-bolt-tiny\refs\main`. El código carga por `model_id` sin revisión explícita, igual que v4.
4. Verifique los hashes:

   ```powershell
   Get-FileHash -Algorithm SHA256 "$env:USERPROFILE\.cache\huggingface\hub\models--amazon--chronos-bolt-tiny\snapshots\a0e552de83495b5c28c14c71c374f3e33280b340\model.safetensors"
   ```

   Deben coincidir con la tabla. `00_verificar_entorno.py` también lo verifica y aborta si no coinciden.

5. Ejecute el experimento normalmente. `lib/entorno.py` fija `HF_HUB_OFFLINE=1` y `TRANSFORMERS_OFFLINE=1`, de modo que no se intenta ninguna descarga.

Alternativa sin internet: copie la carpeta `models--amazon--chronos-bolt-tiny` completa desde un equipo que ya la tenga a la misma ruta de la caché.

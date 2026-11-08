"""Download the Chronos-Bolt weights used in the paper, at the exact Hugging Face revisions.

    python download_chronos_weights.py            # tiny only (rolling-origin backtesting), ~35 MB
    python download_chronos_weights.py --all      # tiny + small + base (diagnostic experiments), ~1.05 GB

The files go to the standard Hugging Face cache (~/.cache/huggingface/hub). The pipeline then runs offline
(HF_HUB_OFFLINE=1) and checks the SHA-256 of the tiny weights against
v2_reentrenamiento/experimentos_backtesting_rodante/01_configuracion/hashes_congelados.json.
"""
import sys

from huggingface_hub import snapshot_download

MODELS = {
    "amazon/chronos-bolt-tiny": "a0e552de83495b5c28c14c71c374f3e33280b340",
    "amazon/chronos-bolt-small": "772f3d25d38aec6d914c8949dab4462e2d46f5d8",
    "amazon/chronos-bolt-base": "5d9f166d69f47aef3401367a7b842e78fe97b121",
}

if __name__ == "__main__":
    wanted = MODELS if "--all" in sys.argv else {"amazon/chronos-bolt-tiny": MODELS["amazon/chronos-bolt-tiny"]}
    for repo_id, revision in wanted.items():
        path = snapshot_download(repo_id=repo_id, revision=revision, allow_patterns=["config.json", "model.safetensors"])
        print(f"{repo_id}@{revision[:12]} -> {path}")

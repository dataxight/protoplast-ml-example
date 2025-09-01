import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from protoplast.scrna.anndata.trainer import RayTrainRunner
    from protoplast.scrna.anndata.torch_dataloader import DistributedAnnDataset
    from scsims import SIMS
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import protoplast
    return


@app.cell
def _():
    import torch
    import numpy as np
    from protoplast.scrna.anndata.torch_dataloader import DistributedAnnDataset
    return


@app.cell
def _():
    import anndata

    def sims_metadata_cb(ad: anndata.AnnData, metadata: dict):
        metadata["num_genes"] = ad.var.shape[0]
        metadata["input_dim"] = metadata["num_genes"]
        metadata["cell_lines"] = ad.obs["cell_line"].cat.categories.to_list()
        metadata["num_classes"] = len(metadata["cell_lines"])
        metadata["output_dim"] = metadata["num_classes"]
    return (sims_metadata_cb,)


@app.cell
def _():
    from scsims.model import SIMSClassifier
    return (SIMSClassifier,)


@app.cell
def _():
    from protoplast.scrna.anndata.torch_dataloader import DistrbutedCellLineAnnDataset as Dcl
    from protoplast.scrna.anndata.trainer import RayTrainRunner
    from ray.train.lightning import RayDDPStrategy
    return Dcl, RayDDPStrategy, RayTrainRunner


@app.cell
def _(Dcl, RayDDPStrategy, RayTrainRunner, SIMSClassifier, sims_metadata_cb):
    trainer = RayTrainRunner(
        SIMSClassifier,                   
        Dcl,                               
        ["input_dim", "output_dim"],      # maps to SIMSClassifier(input_dim, output_dim)
        sims_metadata_cb,
        ray_trainer_strategy=RayDDPStrategy(find_unused_parameters=True)
    )
    return (trainer,)


@app.cell
def _():
    #file_paths = ["/mnt/hdd1/dung/tahoe100/tahoe100_data/plate3_2000_18080.h5ad"]
    file_paths = ["/mnt/ham/dx_data/plate3_filt_Vevo_Tahoe100M_WServicesFrom_ParseGigalab.h5ad"]
    thread_per_worker = 2
    batch_size = 2000
    test_size = 0.2
    val_size = 0.2
    return batch_size, file_paths, test_size, thread_per_worker, val_size


@app.cell
def _(batch_size, file_paths, test_size, thread_per_worker, trainer, val_size):
    trainer.train(file_paths, thread_per_worker, batch_size, test_size, val_size)
    return


if __name__ == "__main__":
    app.run()

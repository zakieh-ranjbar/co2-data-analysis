"""Create reproducible visualizations for the CO2 dataset."""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from .analysis import load_data


def create_plots(input_path: str | Path = "data/co2.csv", output_dir: str | Path = "outputs") -> list[Path]:
    frame = load_data(input_path).rename(columns={"engine":"engine_l","cylandr":"cylinders","fuelcomb":"fuel_combined","out1":"co2_output"})
    out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    paths=[]
    fig, ax = plt.subplots(figsize=(8, 5)); ax.hist(frame.co2_output, bins=24, color="#277da1", edgecolor="white"); ax.set(title="Distribution of CO2 output", xlabel="CO2 output (out1)", ylabel="Vehicles"); fig.tight_layout(); p=out/"co2_distribution.png"; fig.savefig(p,dpi=160); plt.close(fig); paths.append(p)
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5));
    for ax, column, label, color in zip(axes, ["engine_l","cylinders","fuel_combined"], ["Engine size","Cylinders","Combined fuel consumption"], ["#f9844a","#90be6d","#f9c74f"]): ax.scatter(frame[column], frame.co2_output, s=18, alpha=.55, color=color, edgecolors="none"); ax.set(xlabel=label, ylabel="CO2 output (out1)");
    fig.suptitle("Vehicle features vs CO2 output", y=1.02); fig.tight_layout(); p=out/"features_vs_co2.png"; fig.savefig(p,dpi=160,bbox_inches="tight"); plt.close(fig); paths.append(p)
    corr=frame[["engine_l","cylinders","fuel_combined","co2_output"]].corr(); fig, ax=plt.subplots(figsize=(6,5)); im=ax.imshow(corr,cmap="RdYlBu_r",vmin=-1,vmax=1); ax.set_xticks(range(4),corr.columns,rotation=35,ha="right"); ax.set_yticks(range(4),corr.columns); [ax.text(j,i,f"{corr.iloc[i,j]:.2f}",ha="center",va="center",color="black") for i in range(4) for j in range(4)]; fig.colorbar(im,ax=ax,label="Pearson correlation"); fig.tight_layout(); p=out/"correlation_heatmap.png"; fig.savefig(p,dpi=160); plt.close(fig); paths.append(p)
    return paths

if __name__ == "__main__":
    create_plots()

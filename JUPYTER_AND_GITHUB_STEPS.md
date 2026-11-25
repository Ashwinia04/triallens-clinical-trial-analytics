# TrialLens — browser-only setup with Google Colab

You do not need to install Python, Anaconda, or Jupyter on your computer.

## Files to download

- `TrialLens_Clinical_Trial_Analytics_Colab.ipynb` — the notebook to open in Colab.
- `triallens-clinical-trial-analytics-jupyter.zip` — the complete project folder with synthetic data, source code, SQL, tests, and documentation.

## Run in Google Colab

1. Download both files above to your computer.
2. Open <https://colab.research.google.com/> and sign in.
3. In Colab, choose **File → Upload notebook** and select `TrialLens_Clinical_Trial_Analytics_Colab.ipynb`. Google documents this import route in its Colab FAQ.
4. In the opened notebook, run the first setup code cell. When the upload dialog appears, select `triallens-clinical-trial-analytics-jupyter.zip`.
5. Run the dependency-install cell.
6. Choose **Runtime → Run all** or run the remaining cells from top to bottom.
7. Read the tables and charts. Do not skip cells.
8. Save a copy to Google Drive using **File → Save a copy in Drive**. After execution, use **File → Download → Download .ipynb** to save a local copy with outputs.

## Important Colab notes

- Colab executes code on a temporary Google-hosted runtime. Uploaded files in `/content` do not automatically become part of your saved notebook. Keep your ZIP available to upload again if the runtime resets.
- The notebook setup cell unpacks the ZIP to `/content/triallens-clinical-trial-analytics` and changes the working directory automatically.
- The project contains synthetic/fictitious study records only. It is an educational portfolio simulation, not validated clinical software and not evidence of professional trial experience.
- Do not upload real patient or confidential clinical data.

## Publish to GitHub later

Once the notebook runs successfully, upload the complete extracted project folder to a new public GitHub repository. Include the notebook, `data/`, `src/`, `sql/`, `tests/`, `outputs/`, `README.md`, and `requirements.txt`. Do not publish real or confidential data.

## Submission format

---

Your submission should be a ZIP archive containing the following components:

1. An [**image**](https://www.drivendata.org/competitions/256/pale-blue-dot/page/803/#1-image) of your data visualization (`visual.png`)
2. A short [**summary**](https://www.drivendata.org/competitions/256/pale-blue-dot/page/803/#2-summary) of less than 1,800 characters (`summary.pdf`)
3. *(Only required for Best Overall prize)* A [**detailed report**](https://www.drivendata.org/competitions/256/pale-blue-dot/page/803/#3-detailed-report), which can be submitted either as a 1-4 page written report (`report.pdf`) or a video report that is a maximum of 7 minutes long (`report.mp4`). A report is required for a submission to be considered for the Best Overall prize, but is *not* required to be considered for an Honorable Mention for Compelling Visuals.

Your submission can have significant non-visual components as well, as long as there is a visualization involved.

You are only allowed to make one submission. To make changes, you can
 delete and re-upload your submission as many times as you like. Only
the last entry submitted will be considered.

**The ZIP archive of your submission cannot be larger than 100MB.**

Participants can submit individually, or form teams of up to four
people. Participants are encouraged to find teammates through the [competition forum](https://community.drivendata.org/c/pale-blue-dot).

#### 1. Image

Submit a static image showing your data visualization. This file must be named `visual.png`, `visual.jpg`, `visual.jpeg`, or `visual.pdf`.

If your visualization is interactive, you should also submit a short
video demonstration or a URL where the visualization can be viewed. When
 selecting the "Best overall" prize winners, interactive visuals may be
more likely to satisfy the "Impact" metric of the [evaluation criteria](https://www.drivendata.org/competitions/256/pale-blue-dot/page/803/#evaluation) than static images.

* To submit a  **video demo** , include an MP4 file called `visual_demo.mp4`
  that is a maximum of 3 minutes long. If you are submitting the detailed
  report as a video, you may choose to combine the video demo with your
  report rather than providing two separate MP4 files.
* To submit a  **URL** , include the link in your detailed report.

#### 2. Summary

Submit a brief, **1-paragraph written summary** of your submission (1,800 characters maximum). This file must be named `summary.pdf`. Your summary should include:

* A brief description of what your visual shows (1-2 sentences)
* A list of all the datasets you used
* Which Sustainable Development Goal(s) you hope to advance ([zero hunger](https://www.un.org/sustainabledevelopment/hunger/), [clean water and sanitation](https://www.un.org/sustainabledevelopment/water-and-sanitation/), [climate action](https://www.un.org/sustainabledevelopment/climate-change/))
* A list of all the tools you used to build your visualization (e.g., Python, Planetary Computer, etc.)

#### 3. Detailed report

The **detailed report** should describe your methodology and explain how your submission meets each of the [evaluation criteria](https://www.drivendata.org/competitions/256/pale-blue-dot/page/803/#evaluation). Use the prompts provided below to help structure your report to address all of the criteria.

**A detailed report is required to be considered for the Best Overall prize.** However, it is *not* required to be considered for the "Honorable mentions for compelling visuals" [prizes](https://www.drivendata.org/competitions/256/pale-blue-dot/page/802/#honorable-mentions-for-compelling-visuals).

[]()

##### Detailed report prompts

1. How does your visual inform a decision or action that furthers one or more of the key competition SDGs ([zero hunger](https://www.un.org/sustainabledevelopment/hunger/), [clean water and sanitation](https://www.un.org/sustainabledevelopment/water-and-sanitation/), [climate action](https://www.un.org/sustainabledevelopment/climate-change/))?
2. How did you create your submission? Include the tools you used
   (eg. Python, Excel, specific python packages), how you processed the
   data, and (if applicable) how you managed your codebase. If you have a
   public repository with code, you can share a link here.
3. What motivated you to choose this topic?
4. How did you learn about the broader context of your chosen issue
   (e.g., historical, social, political)? This could include drawing on
   the lived experiences of team members, reading articles and literature,
   conducting interviews with community members, etc. Did what you learned
   change your approach?
5. What are the ethics and/or equity issues you considered? What are some possible strategies or approaches for addressing them?
6. Would your team like to share the URL of an interactive visualization?

The report can be submitted as either a written document or a video.
When judging, there will be no preference between written reports and
video reports.

**Written report option**

To submit a written report, include a file called `report.pdf`. Written reports should be:

* **4 pages maximum including figures and tables**
* On paper size 8.5 x 11 inch or A4, with minimum margins of 1 inch
* Minimum font size of 11
* Minimum single-line spacing
* In PDF file format

To create a written report, download the template from the [data download page](https://www.drivendata.org/competitions/256/pale-blue-dot/data/) and simply fill in the answer to each prompt.

**Video report option**

To submit a video report, include a file called `report.mp4`. Video reports should be MP4 files that are  **7 minutes long maximum** .
 Videos are not expected to have professional-level quality and polish,
but should succinctly answer the prompts above. Substance matters more
than slickness. For example, you may submit a simple video of yourself
speaking, or a screen recording with narration. Participants are not
required to appear in their videos.

If your visualization is interactive, you are also allowed to submit a [video demo](https://www.drivendata.org/competitions/256/pale-blue-dot/page/803/#1-image).
 If applicable, you may combine the video demo with your video report
rather than submitting two separate files. In that case, the combined
video can be up to 10 minutes long maximum.

#### Creating a ZIP archive

Below are instructions to create a ZIP archive from your submissions files manually, at the command line, or with Python.

**Manually**

1. Put all of the files you want to include in your submission in one folder.
2. Open the file finder app on your computer.
3. Right-click on the folder and select "Compress". On some operating
   systems, you may have select "Send to", and then "Compressed folder".

**At the command line**

1. Put all of the files you want to include in your submission in one folder.
2. In the command line, run `zip -r path/to/submission/folder path/to/new/zipfile.zip`
   For example, say I have all of my submission files saved in a folder called `submission_files` and I want to save out a zipfile called `latest_submission.zip`. I would run:
   ```
   $ zip -r submission_files latest_submission.zip
       adding: submission_files/ (stored 0%)
       adding: submission_files/visual.png (stored 0%)
       adding: submission_files/summary.pdf (stored 0%)
       adding: submission_files/report.pdf (stored 0%)
   ```

**With Python**

```python
from zipfile import ZipFile

# Define where the zipped file should be saved
save_to = "submission.zip"

# Define the list of files to include
include_files = [
    "submission_files/visual.png", 
    "submission_files/summary.pdf",
    "submission_files/report.pdf"
]

# Define the zip file object and add files
with ZipFile(save_to, "w") as zip_object:
    for file in include_files:
        zip_object.write(file)
```

Once you've got your ZIP file, you're ready to submit! Head over to the [submissions page](https://www.drivendata.org/competitions/256/submissions/extra/107/) to upload your file.

[]()

## Guide to open science

---

> Open science is defined as the principle and practice of making
> research products and processes available to all, while  respecting
> diverse cultures, maintaining security and privacy, and fostering
> collaborations, reproducibility and equity.

Below, we have provided concrete ways to follow the practices of open
 science when creating a data visualization submission. These principles
 explain in more detail how to satisfy the "Integrity" and "Usability"
metrics of the evaluation criteria. To learn even more, register for
NASA's [Open Science 101](https://nasa.github.io/Transform-to-Open-Science/take-os101/) online training program!

#### Practical recommendations

|  ![](https://drivendata-public-assets.s3.amazonaws.com/icon-magnifying-glass-blue.png)  | **Be transparent.**Document and share the steps that you took to create your submission.
Include details like where your data came from and how you computed any
reported statistics so that someone else could recreate your 

| visualization using your original data source.                                                                                                                                                                               |                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| ![](https://drivendata-public-assets.s3.amazonaws.com/icon-chat-blue.png)                                                                                                                                                      | **Collaborate.**Engage with others in the[competition forum](https://community.drivendata.org/c/pale-blue-dot), |
| use the forum to create teams across disciplines and countries, and                                                                                                                                                          |                                                                                                              |
| share your work on the community code board. You could even win the                                                                                                                                                          |                                                                                                              |
| "Community Code Bonus[Prize](https://www.drivendata.org/competitions/256/pale-blue-dot/page/802/#community-code-bonus-prize)"!                                                                                                  |                                                                                                              |
| ![](https://drivendata-public-assets.s3.amazonaws.com/icon-globe-blue.png)                                                                                                                                                     | **Consider in context.**Learn about the context of your chosen issue (historical, social,                    |
| political, etc). This will be easiest if one of your team members is                                                                                                                                                         |                                                                                                              |
| part of the community primarily affected by your chosen issue. However,                                                                                                                                                      |                                                                                                              |
| you could also accomplish this through reading, or through conducting                                                                                                                                                        |                                                                                                              |
| interviews with community members. Think about how the context impacts                                                                                                                                                       |                                                                                                              |
| your work, and in turn how your treatment of the issue could perpetuate                                                                                                                                                      |                                                                                                              |
| inequalities or subvert them.                                                                                                                                                                                                |                                                                                                              |
| ![](https://drivendata-public-assets.s3.amazonaws.com/icon-bars-blue.png)                                                                                                                                                      | **Identify and mitigate biases.**Consider biases in how the datasets you are using were collecting and       |
| in how the visual could be interpreted. Who is represented, and who may                                                                                                                                                      |                                                                                                              |
| be excluded? Come up with ideas for mitigating these risks. For example,                                                                                                                                                     |                                                                                                              |
| suggest limitations for how and when your tool should be used. For a                                                                                                                                                         |                                                                                                              |
| more comprehensive guide check out[Deon](https://deon.drivendata.org/), DrivenData's ethics checklist for data science projects.                                                                                                |                                                                                                              |
| ![](https://drivendata-public-assets.s3.amazonaws.com/icon-unlocked-blue.png)                                                                                                                                                  | **Make it accessible.**Per the submission instructions, use data and submission file formats                 |
| that anyone could access with free software. Think about barriers for                                                                                                                                                        |                                                                                                              |
| accessing and interpreting your work, especially for members of the                                                                                                                                                          |                                                                                                              |
| community primarily affected by the issue and for key decision makers.                                                                                                                                                       |                                                                                                              |
| For example, use simple language that makes it easy for a broad audience                                                                                                                                                     |                                                                                                              |
| to interpret the visual correctly. If more complex accessibility issues                                                                                                                                                      |                                                                                                              |
| like internet access are relevant, you may outline how these could be                                                                                                                                                        |                                                                                                              |
| addressed in the future.                                                                                                                                                                                                     |                                                                                                              |
| ![](https://drivendata-public-assets.s3.amazonaws.com/icon-book-blue.png)                                                                                                                                                      | **Write reproducible code.**If your submission involves a codebase, write your code in a way that            |
| is easy for others to follow or contribute to. This includes using best                                                                                                                                                      |                                                                                                              |
| practice tools for open science like Github. Check out[Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/), DrivenData's standardized Python project structure, for more coding best practices. |                                                                                                              |

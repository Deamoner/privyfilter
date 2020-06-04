# GDPR Privacy Photo Filter
## De-identification of Photos
## Built with :heart: by [Matthew Davis](https://www.linkedin.com/in/tech-lead-matt-davis/) - [linkedin](https://www.linkedin.com/in/tech-lead-matt-davis/) - [github](https://github.com/Deamoner) - [Medium](https://medium.com/@mdavis_71283) - [Youtube](https://www.youtube.com/channel/UCJNZxBqs8ElqouPqAkZLlqg) - [Facebook](https://www.facebook.com/matthewjamesdavis/)
De-identification and Tracking for Photos.

### Use Cases
- GDPR Protection of Photo Sharing Compliance
- Privacy for Machine Learning utilizing Photos
- Ethical Machine Learning - Remove Race/Gender/Skincolor/Generalize

This repo brings the ability for privacy and removing unethical bias from machine learning.
What started out as a fix for GDPR violations, we will focus on testing for racial and other characteristic bias.


### Roadmap

#### v0.1 - Basic Direct Identifier Scrubbing

- Face Detect
- Face Scrub

#### v0.2 - Full Deidentify Photo Process

- Detect other possible identifiers - text etc
- ScrubPIIText
- Pose Detect and Output Data
- Deidentify - Output of only pose and facial feature data in photo

#### v0.3 - Backtest/Unit Test Bias Dataset Creator

- RandomSkincolor
- RandomFaceReplace
- RandomAge


### Methodology

Scrub all identifying and data possible for bias from the dataset keeping a featureset that still allows for useful machine learning.

1. PII Data Check
2. DI(Direct Identifier) Scrubbing - Basic Privacy Preservation
3. Remove Unethical Bias Data - Remove all features but Pose, Facial Expression


### Process for Features

What needs to be done:
1. Scoping - Process, FaceDetect - InProgress Data Science Colab Testing, RandomFaceReplace, FaceScrub, MetaMark, AIMark, GetMetaMark, GetAIMark
2. Test Implementation for AI Model pieces - Colab Notebook of Models with Validation Data
3. Library wrapping and Implementation
4. Library Publish


Tasks:
- [x] Face Detect - Colab Testing - Included in the Notebook folder in the repo.
- [X] Facescrub - Colab Testing - Simplest De-identification - Simple blur - Commonly available
- [X] Face Location Extraction
- [ ] Basic Library Object Implementation
- [ ] v0.1 Release for George Floyd Implementation
- [ ] Pose Extraction
- [ ] Location and Meta Information Scrub
- [ ] Race Scrub
- [ ] MetaMark - Direct Implementation no datascience required
- [ ] getMetaMarks - Direct Implementation
- [ ] run - Runs the scanning for faces, scrubbing, and applies metamarks
- [ ] v0.5 Release - Library can now take photos and auto De-id them
- [ ] getPII - get's all the PII in text on the page
- [ ] scrubPII - Will scrub the PII in the image - simple blur
- [ ] Update run functions configs to utilize all functions
- [ ] v0.8 Release - Automated Privacy Picture Scrubbing with Faces and text - handles most public access scenarios
- [ ] RandomFaceReplace - Synthetic face generation for hidden in plain sight Privacy
- [ ] alterPII - Simple word replacement for hidden in plain sight
- [ ] v0.9 Release - Hidden in plain sight photo de-identification
- [ ] AIMark - Mark through the pixels in a secret method a way to identify the source and downloader of the photo
- [ ] getAIMark - Retreive this secret marking


## Installation - Not working yet

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Privy - Privacy Photo Filter library.

```bash
pip install privyfilter
```

## Usage

```python
from privyfilter.privyfilter import Privyfilter as pf

faces2, img = pf.faceScrub("../TestPics/1Person-Close.jpg")

```

## Deploying Module

```
twine upload dist/*
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

# GDPR Privacy Photo Filter
## De-identification of Photos
## Built with :heart: by [Matthew Davis](https://www.linkedin.com/in/tech-lead-matt-davis/) - [linkedin](https://www.linkedin.com/in/tech-lead-matt-davis/) - [github](https://github.com/Deamoner) - [Medium](https://medium.com/@mdavis_71283) - [Youtube](https://www.youtube.com/channel/UCJNZxBqs8ElqouPqAkZLlqg) - [Facebook](https://www.facebook.com/matthewjamesdavis/)
Filtering photos for privacy and bias(racial, gender) for machine learning.

### Use Cases
- GDPR Protection of Photo Sharing Compliance
- Privacy for Machine Learning utilizing Photos
- Ethical Machine Learning - Remove/Generalize Race/Gender/Skincolor/Generalize

Privy filter is made to remove private data from photos and to give the method for
removing or accomodating for unethical bias in data.


### Roadmap

#### v0.1 - Basic Direct Identifier Scrubbing - Done

- Face Detect - Needs improvement
- Face Scrub

#### v0.2 - Identify other identifiers and bias features

- Detect skin - Dataset: http://cs-chan.com/downloads_skin_dataset.html
- AdjustSkin - Can adjust skincolor to generate new dataset photo
- Fixes and Testing for faceDetect

#### v0.3 - Backtest/Unit Test Bias Dataset Creator

- DetectText
- ScrubText
- Fixes for DetectSkin and AdjustSkin

#### v0.4 - Backtest/Unit Test Bias Dataset Creator

- SyntheticFaceGenerate - Morph thee existing faces into others - can generalize or specify a style transfer from our baseline
- SyntheticFaceReplace
- genderDetect

#### v0.5 - Backtest/Unit Test Bias Dataset Creator

- createBalancedPhotoSet - Takes 1 photo and creates the balance extra number of photos near to remove bias from training.
- sythethicGendersReplace

### Methodology

Scrub all identifying and data possible for bias from the dataset keeping a featureset that still allows for useful machine learning.

1. PII Data Check
2. DI(Direct Identifier) Scrubbing - Basic Privacy Preservation
3. Remove Unethical Bias Data - Remove all features but Pose, Facial Expression
4. Create alternatives synthetic photos for balanced training


### Process for Features

What needs to be done for roadmap Contribution:
1. Scoping
2. Test Implementation for AI Model pieces - Colab Notebook of Models with Validation Data
3. Library wrapping and Implementation
4. Library Publish


Tasks:
- [x] Face Detect - Colab Testing - Included in the Notebook folder in the repo.
- [X] Facescrub - Colab Testing - Simplest De-identification - Simple blur - Commonly available
- [X] Face Location Extraction
- [X] Basic Library Object Implementation
- [X] v0.1 Release for basic Direct Identifiers
- [X] Pose Extraction Notebook
- [X] Basic Skin Extraction
- [ ] Improved SkinExtraction Protocol
- [ ] Skin Adjustment Methodology
- [ ] Fixes for face detection to
- [ ] Basic pose and feature extraction for totally scrubbed photos
- [ ] v0.2 Release for George Floyd Implementation


## Installation

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

# Photo Filter for racial/ethical bias
### Remove or change attributes of photos the could cause bias or issue.
### Create a balanced dataset for machine learning without compliance or ethical violations.
## Built with :heart: by [Matthew Davis](https://www.linkedin.com/in/tech-lead-matt-davis/) - [linkedin](https://www.linkedin.com/in/tech-lead-matt-davis/) - [github](https://github.com/Deamoner) - [Medium](https://medium.com/@mdavis_71283) - [Youtube](https://www.youtube.com/channel/UCJNZxBqs8ElqouPqAkZLlqg) - [Facebook](https://www.facebook.com/matthewjamesdavis/)
Filtering photos for privacy and bias(racial, gender) for machine learning.

### Use Cases
- GDPR Protection of Photo Sharing Compliance
- Privacy for Machine Learning utilizing Photos
- Ethical Machine Learning - Remove/Generalize Race/Gender/Skincolor/Generalize

Privy filter is made to remove private data from photos and to give the method for
removing or accomodating for unethical bias in data.

![privyfilter detect and blurr faces](https://github.com/Deamoner/privyfilter/raw/master/TestPics/privyfilter.jpg)
![privyfilter detect and blurr faces](https://github.com/Deamoner/privyfilter/raw/master/Results/pipeline.png)



### Latest Release:
v0.16 - RemoveMeta - Remove the Meta Data from photos

### Next Release - alpha - bugs in loading the model
v0.2 - Sythetic Face Generation and Face Swapping

### Roadmap

#### v0.1 - Basic Direct Identifier Scrubbing - Done

- Face Detect - Needs improvement
- Face Scrub

#### v0.1.6 - Basic Meta Data Scrubber - Done

- RemoveMetaData(imgPath)

#### v0.2.0 - Identify face and replace - Alpha - Cleaning up the code.

- getRandomFakeFace : get Random Synthetic Face - done - needs tmp folder setting
- peopleObject - getFaceInfo - done - face model not loading on
- peopleObject - swapFace(img1, img2) -

#### v0.3.0 - Identify other identifiers and bias features

- Detect skin - Dataset: http://cs-chan.com/downloads_skin_dataset.html
- AdjustSkin - Can adjust skincolor to generate new dataset photo

#### v0.3 - Direct Aging

- Test Face Aging Algo
- Test Gender Changing Algo
- Testing Race Direct Synthetic Style Transfer
- Fixes for DetectSkin and AdjustSkin

#### v0.4 - Full Balanced Dataset Creator

- Update Accuracy of getDemographics
- CreateBalancedPhotos(img)
-

#### v0.5 - Improve Accuracy and Speed

- Baseline of Full Pipeline per Photo
-

### Methodology

Scrub all identifying and data possible for bias from the dataset keeping a featureset that still allows for useful machine learning.

1. Identify Features - Faces, People
2. Remove Unethical Bias Data - New Synthetic Faces, Adjust Skin
3. Create alternatives synthetic photos for balanced training

## References Work

- https://towardsdatascience.com/survey-d4f168791e57
- https://brie.berkeley.edu/sites/default/files/brie_wp_2018-3.pdf
- https://www.brookings.edu/research/algorithmic-bias-detection-and-mitigation-best-practices-and-policies-to-reduce-consumer-harms/
- https://healthitanalytics.com/news/eliminating-racial-bias-in-algorithm-development

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
- [X] Synthetic Face Generation
- [X] Face Swap Testing
- [X] Face Swap Integration into main library
- [X] Fixes for model automated download
- [ ] Clean up API for people and privyfilter library to match specs.
- [ ] Replace Faces - Replace all faces in photos
- [ ] Improved SkinExtraction Protocol
- [ ] Skin Adjustment Methodology
- [ ] Fixes for face detection to
- [ ] v0.2 Release for George Floyd Implementation


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Privy - Privacy Photo Filter library.

```bash
pip install privyfilter
```

## Basic Usage

```python
from privyfilter.privyfilter import Privyfilter as pf

faces2, img = pf.faceScrub("../TestPics/1Person-Close.jpg")

```

## Scrub Meta Data
```python
from privyfilter.privyfilter import Privyfilter as pf
img = pf.RemoveMetaData("../TestPics/1Person-Close.jpg")
```

## Face Swap - Inputs imgPath
```python
swapimg = pf.swapFaces("../TestPics/1Person-Close.jpg", "../TestPics/2Person-Close.jpg")
cv2_imshow(swapimg)
```

## EndGoal API:
   privyfilter.findFaces(imgpath, demographics=false) or privyfilter.findFaces(cv2 object)
    returns array of faces and can include demographics.
   privyfilter.scrubFaces(imgPath) or privyfilter.scrubFaces(cv2 object)
    returns faces, and scrubbed img
   privyfilter.swapFaces(img1Path, img2Path) or privyfilter.swapFaces(img1 cv2 object, img2 cv2 Object)
    - replaces all faces in 2nd image with first. Returns new image as cv2 Object.
   privyfilter.getFakeFace()
    returns fakeface image object
   privyfilter.replaceFaces(img1)
    returns img of all faces randomly replaced with fake ones.


## Deploying Module

```
python setup.py bdist_wheel --universal
twine upload dist/*
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

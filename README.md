# Photo Filter for racial/ethical bias
### Filtering photos for bias(racial, gender) for machine learning.
### Privy filter is your photo dataset augmentor and analyzer for unethical bias(Race, Gender, Age)
## Built with :heart: by [Matthew Davis](https://www.linkedin.com/in/tech-lead-matt-davis/) - [linkedin](https://www.linkedin.com/in/tech-lead-matt-davis/) - [github](https://github.com/Deamoner) - [Medium](https://medium.com/@mdavis_71283) - [Youtube](https://www.youtube.com/channel/UCJNZxBqs8ElqouPqAkZLlqg) - [Facebook](https://www.facebook.com/matthewjamesdavis/) - [Privy Filter Demo](https://privyfilter.herokuapp.com/)
Filtering photos for bias(racial, gender) for machine learning.

### Demo

Privy Filter: [Info and Demo Site](https://privyfilter.herokuapp.com/)

### Use Cases
- Train Machine Learning Models minimizing unethical bias inherent in underlying photo dataset - IE Race, Gender, Age Discrimination
- Data Augmentation of Photo datasets to balance unethical data bias
- Create and Identify Unit Test Photos for datasets to ensure continual testing of bias in classification type problems
- Ethical Machine Learning - Remove Identity/Generalize Identinity/Generalize Race/Gender/Skincolor/Generalize

Privy filter is your photo dataset augmentor and analyzer for unethical bias(Race, Gender, Age)

![privyfilter detect and blurr faces](https://github.com/Deamoner/privyfilter/raw/master/TestPics/privyfilter.jpg)
![privyfilter detect and blurr faces](https://github.com/Deamoner/privyfilter/raw/master/Results/pipeline.png)



### Latest Release:
v0.2 - Sythetic Face Generation and Face Swapping

### Roadmap

#### v0.1 - Basic Direct Identifier Scrubbing - Done

- Face Detect - Needs improvement
- Face Scrub

#### v0.1.6 - Basic Meta Data Scrubber - Done

- RemoveMetaData(imgPath)

#### v0.2.0 - Identify face and replace - Done

- getRandomFakeFace : get Random Synthetic Face - done - needs tmp folder setting
- peopleObject - getFaceInfo - done - face model not loading on
- peopleObject - swapFace(img1, img2)

#### v0.3.0 - ProcessAll and Use Case Direct Finishing

- processOne() - review demographics of current photo - suggest additional photos
- generatePhoto - from one photo and demographic info - generate those new photo demographic utilizing synthetic faces
- processDir() - process all the photos in the directory - first calculate the statistics and distributions - and parameterize a directory to save all sythetic balanced photos.
- Update DemoSite with Use Case direct notes and usability examples

#### v0.4.0 - Identify other identifiers and bias features

- Detect skin - Dataset: http://cs-chan.com/downloads_skin_dataset.html
- AdjustSkin - Can adjust skincolor to generate new dataset photo
- Update processone stats and generatephoto to utilize skincolor data and manipulation
- Update demosite with video
- Demo of CelebA Dataset

#### v0.5 - Direct Aging and Gender

- Test Face Aging Algo
- Test Gender Changing Algo
- Testing Race Direct Synthetic Style Transfer
- Fixes for DetectSkin and AdjustSkin

#### v0.6 - Improve/Increase Original Photoset data quality retention through improve synthetic matching

- Face pose matching for synthetic face replacement
- Review accuracy of underlying demographic model
- New CelebA Demo

#### v0.7 - Increase compatibility of pipeline for photosets

- Support for multi face photo - Scoping - Document API updates
- Support for people but no face in photos - recognize poses without faces

#### v0.8 - Reliability Fixes

- Back to baseline of usecase documentation
- Use Case Automated Testing
-

### Methodology

Scrub all identifying and data possible for bias from the dataset keeping a featureset that still allows for useful machine learning.

1. Identify Features - Faces, People
2. Remove Unethical Bias Data - New Synthetic Faces, Adjust Skin, Gender and Age Transformation
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
- [X] Clean up API for people and privyfilter library to match specs.
- [X] Replace Faces - Replace a face in a photo
- [ ] Scope out API for calculation and methodology of race/gender face demographic balancing
- [ ] Functions to process one photo for demographics and balanced demographics needed return
- [ ] Function generateSytheticPhoto - create the photo required
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
   - privyfilter.processDir(srcPath, dstPath) - analyze all photos for demographics in srcdirect, if dstdirect - generate the balanced dataset)
   - privyfilter.processOne(srcPath, dstPath) - analyze photo and suggest demographics of balanced photo dataset - if dstpath then generate
   - privyfilter.generatePhoto(srcPhoto, demographic, dstPath) - generate a photo from the original with the demographic params specified  
   - privyfilter.findFaces(imgpath, demographics=false) or privyfilter.findFaces(cv2 object)
    - returns array of faces and can include demographics.
   - privyfilter.scrubFaces(imgPath) or privyfilter.scrubFaces(cv2 object)
    - returns faces, and scrubbed img
   - privyfilter.swapFaces(img1Path, img2Path) or privyfilter.swapFaces(img1 cv2 object, img2 cv2 Object)
    - replaces all faces in 2nd image with first. Returns new image as cv2 Object.
   - privyfilter.getFakeFace()
    - returns fakeface image object
   - privyfilter.replaceFaces(img1)
    - returns img of all faces randomly replaced with fake ones.

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

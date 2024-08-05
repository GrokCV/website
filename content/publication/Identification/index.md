---
title: "Identification method of freshwater fish species using multi-kernel support vector machine with bee colony optimization."
authors:
- admin
- Wu Yiquan
- Yin Jun
- Dai Yimian
- Yuan Yongming
author_notes:
- 
-
- 
-

date: "2014-08-15T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2014-08-15T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Transactions of the Chinese Society of Agricultural Engineering"
publication_short: ""

abstract:  Currently, the identification of freshwater fish species is conducted by people. Computer vision techniques can solve problems existing in identification by hand, such as a large amount of work and low precision. Firstly, freshwater fish are converted into an image signal. Then images are transmitted to the computer processing system to be analyzed and processed. The features of freshwater fish images are extracted, and the movements of the equipment are controlled according to the features. As a result, the production efficiency and production quality are improved by this substitute for the manual work. Thus, in order to identify freshwater fish species automatically and accurately, computer vision techniques are adopted and an identification method based on Krawtchouk moments, a gray level co-occurrence matrix, and a multi-kernel least squares support vector machine (LS-SVM) with bee colony optimization is proposed. Firstly, gray level images of freshwater fish samples are obtained by camera, image acquisition card, and PC. Secondly, shape features such as the length to width ratio of freshwater fish and Krawtchouk moment invariants are calculated. The length to width ratio can be obtained by looking for the minimum circumscribed rectangle of fish. The fish head, fish body, and fish tail are obtained based on the minimum circumscribed rectangle. Then the Krawtchouk moment invariants of the fish head and those of the fish tail can be obtained. Thirdly, four characteristic parameters such as angular second moment, entropy, deficit moment, and variance based on a gray level co-occurrence matrix of the fish body are calculated, which are used as texture features. Finally, the above shape features and texture features are combined into a high dimensional feature vector. The feature vector is input into multi-kernel LS-SVM. In a multi-kernel LS-SVM, a polynomial kernel function and radial basis function kernel are used, which can make up for limitations of a single kernel function. The artificial bee colony algorithm is used to optimize the undetermined parameters in a multi-kernel LS-SVM. The identification accuracy of the test sample serves as a fitness function. The optimum parameters are output once the identification accuracy attains its maximum. Five freshwater fish species such as bream, bighead, crucian carp, grass carp, and black carp are identified by using the proposed method. A total of 190 fish were used as the research object. Among them, 70 fish were used as training samples, and the remaining 120 fish were used as testing samples. The experimental results showed that when bream, bighead, crucian carp, and grass carp are identified, the identification accuracy of them can all reach more than 95.83%. When bream, bighead, crucian carp, and black carp are identified, the identification accuracy of them can all reach more than 91.67%. When bream, bighead, crucian carp, grass carp, and black carp are identified, the identification accuracy of them can all reach more than 83.33%. In comparison with the freshwater fish identification method proposed recently, the back propagation (BP) neural network method, and the single kernel LS-SVM method, the proposed method has the higher identification accuracy. It indicates that the above shape features and texture features extracted can reflect the information of freshwater fish more comprehensively and effectively. Furthermore, the performance of a multi-kernel LS-SVM is much better than that of a single kernel LS-SVM. The proposed method is expected to find wide applications in a freshwater fish processing system.

# Summary. An optional shortened abstract.
summary: 

tags:
- CV
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.ingentaconnect.com/content/tcsae/tcsae/2014/00000030/00000016/art00040


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

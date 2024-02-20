# Whale Sound Detection

## Intro

The commercial marine industry is a major contributor to whale death and disruption. In an effort to reduce this industries harm, Marinexplore and Cornell University collected hydrophone recordings with and without whale calls in the North Atlantic with the eventual hope of building hydrophones with compute onboard to live detect whales to prevent collisions. In 2013, Cornell University posted a competition for the most accurate ML models to identify whale calls in these recordings. I wish to try solving this problem using the advances in machine learning in the last decade.

## Approach

My minimum viable project will be running k-nearest neighbor on the image version of the dataset. I wish to do this with scikit learn to better mirror what I would do in industry. This would also allow me to use K-D Tree to reduce the computation time of each prediction and make even the MVP novel from classwork. I did not see any use of k-nearest neighbors so this will be a novel model for this problem. I do not expect this model to perform well, however, it lets me start working on this project in familiar territory that closely mirrors what we have done in class.

My primary goal will be running ResNet on the image version of the dataset. Resnet is a general-purpose image recognition CNN, that is used by many real-world specialized tasks by retraining the model to a particular task. Resnet is a complex CNN. 

At the time of the competition, ResNet did not exist, so I will be doing novel work. However, a pre-pre-curser to ResNet, LeNet-5, was effectively applied in a project submission I read. Because both ResNet and LeNet-5 were trained on the same dataset (ImageNet) and are used in the same way (general purpose image categorization CNN that is retrained to specific tasks), I believe this is a reasonable balance between feasible and novel.

My stretch goal is to build my own CNN model to on the image version of the dataset using Keras. I will closely model my stretch goal to what we did in class and in our final. I do not see this task as any more work than my main goal, but I wish to priorities the work that will help me with my comps.

## Evaluation

Because there are only two categories, and my data is labeled evaluation will be straight forward. I will also use the evaluation metric proposed by the competition; Area Under the Curve which is created by combining the true positive rate with the false positive rate. I will also create confusion matrixes for each model.

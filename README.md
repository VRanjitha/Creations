# whizzKid

hey friends!
I'm ranjitha and i am very much interested in making PREDICTIONS. This interest got me here..


# Purpose
    >The main aim is to allow the computers learn automatically without human intervention and adjust actions accordingly.
    >machine learning technology is applied in various sectors like:
    -HEALTH CARE
    -FINANCIAL
    -BANKING
    -AGRICULTURAL SECTORS.etc
    >The above given codes are some of the machine learning projects for BEGINNERS.

# Important Libraries
    > os: To interact with operating system
    >numpy : To work with arrays and matrix processing
    >pandas :To work with csv files and specifically developed for data extraction and preparation
    >matplotlib: To visualize data and To create charts using pyplot module
    >sklearn.model_selection: train_test_split module to split the dataset into training and testing data.

# Machine Learning Algorithms
   # Linear Regression : Predictions are continuous values
       -In ML, we have a set of input variables (x) that are used to determine the output variable (y). A relationship exists between the input variables and the output variable. 
       -The goal of ML is to quantify this relationship.
   # Logistic Regression : Predictions are descrete values
       - best suited for binary classification (datasets where y = 0 or 1, where 1 denotes the default class.
       -the output is in the form of probabilities of the default class.
   # Navie Bayes :
      -To calculate the probability that an event will occur, given that another event has already occurred, we use Bayes’ Theorem.
   # K Nearest Neighbors(KNN)    :
      - uses the entire dataset as the training set, rather than splitting the dataset into a trainingset and testset.
      -the algorithm goes through the entire dataset to find the k-nearest instances to the new instance, or the k number of instances          most similar to the new record and outputs the means.
   # Support Vector Machine (SVM) : 
      - classification to plot raw data as points in an n-dimensional space.
   # Decision Tree Classifier:
      -This uses the tree representation to solve the problem in which each leaf node corresponds to a class label and attributes are          represented on the internal node of the tree.
   # Random Forest:
      -Random Forest i.e. multiple learners is an improvement over bagged decision trees i.e. a single learner.
   # Adaboost Classifier:
      -Ada-boost classifier combines weak classifier algorithm to form strong classifier.
     - we combine multiple classifiers with selection of training set at every iteration and assigning right amount of weight in final.
# STEPS:
  # 1. Import libraries
    -to import all the required libraries to proceed with the project
  # 2. Import dataset
    -to import the required dataset to proceed with the project(datasets can be downloaded from kaggle)
    -read_csv() is used to read dataset.
  # 3.Observe and understand the data
    -this step includes describe(),info(),construction of correlation matirx,histograms,bar plot, etc.
  # 4.Data processig
    - if in case of existence of any categorical columns must be converted to columns with values 0's and 1's.
    -example: GENDER(male-0,female-1)
    -can be acheived using get_dummies() from pandas library.
  # 5.Apply algorithms
     -apply algorithms that are suitable for the project and build a model.
     -calculate the accuracy of the model. this can be acheived through accuracy_score() from sklearn.metrics.
  # 6.Conclusion
    -finally compare all the models that are built and find the model that gives the highest accuracy.
     

# UNDERSTANNDING of the problem teleCust1000t

The goal is to build a model that will predict a new case or unknown case by using 

- demographic data (ind. variables) such as region, tenure, age ... . and 

- the target variable whitch is "custcat" (Customer Category) .
    - therefore, this (Customer Category) variale is divided by 4 (
      1. Basic Service,
      2. E-Service,
      3. Plus Service,
      4. Total Service).
- My goal is to predict into whitch subcategories, the new client or the unknown client will be in, base on the demographic profile. This is a **multi-class classification problem** (a client belongs to only one category at a time).
- I will use KNN.

# HOW KNN WILL Work 
- He will calculate the distance beteweewn each provided information of the new user and the existing ones by using euclidien distance.
-  instead of sort the all data, witch not convenient, He will sort the most close (neighbors) to see from who the distance is short. to have the close neighbors, we define k = 3
-  Finally once he know from whom the new new user is close, he allow him into that categorie either
      1. Basic Service,
      2. E-Service,
      3. Plus Service,
      4. Total Service)



# KNN  effectivenness
- I used correlation matrix to make sure to select only feature close the target
- then i standartize because even if we have features close to the target the values can be very high for some and others
- to finding the exact K, I have just done sqrt(total_sample)


###### ========================================================================================================================
# Accuracy Results interpretation base on K

## for k = 3 : Test set Accuracy:  0.315
    - with the test data provided (20%), the model correctly predicted the category of 31.5% of the clients 
    Illustration:
        - so if i give now 100 data to my model, he will guess the category for  31 or 32 customer and do mistake on the rest
Conclusion : the model is not fine with k=3

## for K=6 Test set Accuracy:  0.31 
  - the model predicted correctly the category of 31% (0.31) of the giving test data 
    Illustration:
        - so if i give 100 data he will guess the category of 31 user/customuers, and do the mistake on the rest 
Conclusion : the model is not fine with k=6

# Choosing the correct value of k (I have just done sqrt of all sample data) the I got k=37
    # for K=37 the result best_accuracy is 0.41
        - with 0.41, the model is not still good at this point. because he can predict correcttly the category of  41% from the
            given test data. but he will be wrong on the rest (59%).
    # Illustration
        - if i give 100  test data to the current model, he predict correctly 41 but will be wrong on the 59.

# Action : possible reasons and next steps
## possible reasons
    - the direct reason of this is the curse of dimentioannality (because we are using all demographic features withouth filtering)
    - the model is using k=37 it's too much because when the numbers of K is so much the model will have to much nearest neighbors and in that case he will lose the notion of nearest and get confuse.
## next steps
- The ways to  fix that and have and better accuracy is to apply on our data some techniques such as features engineering (FE) or PCA
(Principal component analysis)
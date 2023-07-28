# Sensor-Fault-Detection

### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.


## Deployment Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536973-4530fe7d-5509-4609-bfd2-cd702fc82423.png)


### Step 1: Install the requirements
```bash
pip install -r requirements.txt
```
### step2 - data_dump.py
```bash
we have creat file name data_dump.py in which we have established connection with mongodb database and dump data in database.
```

### step3 - utils.py
```bash
Here we have make some important function which will help in our component part.
```

### step4 - Census 
```bash
In this folder we have creat our Components folder and entity folder and pipeline folder.
```

### step5 - entity
```bash
Here we have two file one is artifact_entity.py and another is config_entity.py config_entity.py - Here we store some important input like what all input it takes while initiating our class example in data_ingestion.py file it will take training_pipeline class which help us to make artifact directory in current directory and also store some pre define path. artifact_entity.py - Here we store output of our component files like generally we store file path and all here.
```

### step6 - Component
```bash
Here we have define cycle of machine learning model-
```

* data_ingestion.py: In this phase we will get our data from mongodb database with the help of get_datafram_as_df function which we have define in "utils.py" and after getting data we perform some cleaning of data then we will save our data in csv file in "feature store" inside "dataingestion" directory and here we also done splitting our data in train and test so this data can further we use for data validation and transformation and all phase so we have also save our train and test data in train.py and test.py file in "dataset" directory which is inside of "dataingestion" directory inside artifact directory.


* data_validation.py: In this phase we will validate our new data with previous data like here we check missing columns and data drift and all , and we store this validation report in a report.yaml file and save that file in "data_validation" directory in artifact directory and path of this file save in "data_validation" class insdie artifact_entity.py file.

* data_transformation.py: In this phase we will transform our data according to our EDA which we have done in jupyter notebook like all preprocessing steps like scalling our data encoding our target column and also convert cat column to numerical with the help of ordinal encoder and all and save all these object in our "data_transformation" directory inside artifact director and path of these object inside "DataTransformationArtifact" class in artifact_entity.py file.

* model_trainer.py: In this phase we will train our model on random forest algorithm and save our model in artifact folder and path is saved in "ModelTrainerArtifact" class in "model_trainer" directory insdie artifact directory and path of our model stored in "model_trainer" class inside artifact_entity.py file.

* model_evaluation.py: Here we compare our new model with previous model which is already in prodution for this we have made some function in our predictor.py file like "get_latest_model" this will fetch our currently trained model and "get_latest_save_model" this will fetch previous trained model which store in saved model directory save for transformation object and all then we will compare our both model if our currently trained model is better than previous trained model than we will go for model pusher phase and we will save our new model if not then it will gives us a error that "current trained model is not better than previous model".

* model_pusher.py: Here we just save our new model and all transformation object which will help us in prediction.

### step7 - pipeline
* Here we made two file one is for training our model and onother for batch prediction- training_pipeline.py - In this file we have just write our code in sequance like we have mention data_ingestion phase first then validation than transformation and so on. batch_prediction.py - In this file we have just made prediction of given file and send back to prediction directory and save it their.

### step8 - main.py
* With this file we can trigger our batch prediction pipeline and training_pipeline.py

### step9 - batch_predicition.py
* First uncomment this batch prediction line if it is commented in main.py file than trigger it it will take a file path for which you want to make predicition simply give it that path and trigger main.py file predicition will start after predicition predicted file save in prediction directory

### step10 - 
* Deployement we have used docker here and with the help of github action we have made our work automate after deployement we can access our airflow so that we can shedule our training pipeline and batch_prection pipeline from their.

MLFLOW_TRACKING_URI = 'file:///C:/Users/DELL/End2End_DS_Projects/JobTechGuide/models/mlruns'
MLFLOW_RUN_ID = "336de09f80cb4d16935f30f82e1e6ed8"
CLUSTERS_YAML_PATH = r"C:\Users\DELL\End2End_DS_Projects\JobTechGuide\data\processed\features_skills_clusters_description.yaml"

#___________________________________________________________________________________

from JobPrediction import JobPrediction
from flask import Flask, request, jsonify

#___________________________________________________________________________________


# Initiate API and JobPrediction object
app = Flask(__name__)
job_model = JobPrediction(mlflow_uri=MLFLOW_TRACKING_URI,
                          run_id=MLFLOW_RUN_ID,
                          clusters_yaml_path=CLUSTERS_YAML_PATH)


# Create prediction endpoint 
@app.route('/predict_jobs_probs', methods=['POST'])
def predict_jobs_probs():
    available_skills = request.get_json()
    predictions = job_model.predict_jobs_probabilities(available_skills).to_dict()
    return jsonify(predictions)


# Create simulation / recommendation endpoint
@app.route('/recommend_new_skills', methods=['POST'])
def recommend_new_skills():
    request_details = request.get_json()
    available_skills = request_details['available_skills']
    target_job = request_details['target_job']

    recommended_skills = job_model.recommend_new_skills(available_skills, target_job).to_dict()
    return jsonify(recommended_skills)

if __name__ == '__main__':
    app.run(port=5000)





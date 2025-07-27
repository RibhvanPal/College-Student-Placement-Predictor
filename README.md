<h1>College Placement Predictor</h1>

<h2>Overview</h2>
<p>A web app built with Flask and Python to predict college student placement using an SVM model based on academic and non-academic factors.</p>

<h2>Features</h2>
<ul>
  <li>User-friendly form for 8 input features (IQ, CGPA, Soft Skills, etc.).</li>
  <li>SVM model with SMOTE and StandardScaler.</li>
  <li>Responsive design with Tailwind CSS and a background image.</li>
</ul>

<h2>Dataset</h2>
<p><a href="https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset" target="_blank">College Student Placement Factors Dataset</a></p>

<h2>Background Image</h2>
<p><a href="https://unsplash.com/photos/brown-concrete-building-under-blue-sky-during-daytime-gnj9vj--FRY" target="_blank">Brown Concrete Building</a> by Unsplash User</p>

<h2>Project Structure</h2>
<pre>
college-placement-predictor/
├── static/college_image1.jpg  # Background image
├── templates/index.html       # Form template
├── model.pkl                 # Trained SVM model
├── scaler.pkl                # Feature scaler
├── main.py                   # Model training script
├── app.py                    # Flask app
├── college_student_placement_dataset.csv  # Dataset
└── README.md                 # This file
</pre>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.8+</li>
  <li>pip</li>
  <li>Web browser</li>
</ul>

<h2>Installation</h2>
<ol>
  <li>Clone: <code>git clone https://github.com/RibhvanPal/College-Student-Placement-Predictor.git</code></li>
  <li>Install: <code>pip install flask pandas scikit-learn imblearn numpy</code></li>
  <li>Add dataset: Download from the dataset link and place as <code>college_student_placement_dataset.csv</code>.</li>
  <li>Add image: Download from the background image link and save as <code>static/college_image1.jpg</code>.</li>
  <li>Train model: <code>python main.py</code></li>
  <li>Run: <code>python app.py</code> (Access at http://localhost:5000)</li>
</ol>

<h2>Usage</h2>
<ul>
  <li>Enter IQ (80–150), CGPA (2–10), and other features.</li>
  <li>Click "Predict Placement" for results.</li>
</ul>

<h2>License</h2>
<p>MIT License</p>

<h2>Contributing</h2>
<p>Submit issues or pull requests on <a href="https://github.com/RibhvanPal/College-Student-Placement-Predictor" target="_blank">GitHub</a>.</p>

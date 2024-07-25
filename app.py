from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///icheckgate_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class SystemModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query']
    response = fetch_response(user_query)
    return jsonify({'response': response})

def fetch_response(query):
    query = query.lower()

    # Keywords and their responses
    keywords = {
        "it infrastructure consultancy": "iCheckGate offers IT infrastructure consultancy to help organizations optimize their IT environment.",
        "ibox": "iBOX™ is a comprehensive solution designed to manage and monitor IT infrastructure efficiently.",
        "mdss": "mDSS™ is a Decision Support System that aids in making informed decisions by analyzing large datasets.",
        "mcheck": "mCheck™ is a product designed for ensuring compliance and monitoring critical IT infrastructure components.",
        "minetag": "MINETag™ is a tagging system that helps in asset tracking and management.",
        "rfid hand-held reader": "The RFID Hand-held Reader is a device used for reading RFID tags for efficient tracking and management.",
        "malert": "mAlert™ Health Monitoring System is designed to monitor health parameters and alert users about critical conditions.",
        "contact": "You can contact iCheckGate via email at contact@icheckgate.ai or call them at +123-456-7890.",
        "benefits": "Using iCheckGate's services offers benefits like improved IT infrastructure management, better decision-making with mDSS™, and enhanced asset tracking with MINETag™.",
        "business model": "iCheckGate™ is a Commercial Off-The-Shelf (COTS) software product developed by MARGSOFT, designed for System Integrators in various domains including Smart City, Mining, and more.",
        "cots licensing": "iCheckGate™ operates under a Commercial Off-The-Shelf (COTS) licensing model, providing ready-to-use software for System Integrators in domains like Smart City, Mining, and more.",
        "maintenance services": "iCheckGate™ provides ongoing maintenance throughout the contract period, including proactive support and timely updates to ensure peak performance.",
        "end-to-end execution process": "The end-to-end execution process for iCheckGate™ includes project initiation, deployment, and meticulous oversight of each phase to ensure successful integration into existing mining infrastructure.",
        "awards": "iCheckGate™ has received several awards including: 1) PLATINUM AWARD in Digital India Award - 2022 for Digital Initiative for Ease of Doing Business, 2) GOLD AWARD in National Award for e-Governance - 2022 for Excellence in Government Process Re-engineering for Digital Transformation, 3) ET-DIGITECH Awards - 2023 for Innovative Use of Technology in e-Governance, 4) TECHNICAL SABHA EXCELLENCE Awards - 2023 for Artificial Intelligence (A.I.), and 5) CSI SIG e GOVERNANCE Award - 2021 for Implementation of MINEMITRA (End to End Mineral Management System).",
        "icheckgate": "iCheckGate is a company providing comprehensive IT infrastructure consultancy and various innovative products."
    }


    for keyword, response in keywords.items():
        if keyword in query:
            return response

   
    service = Service.query.filter(Service.name.ilike(f"%{query}%")).first()
    if service:
        return service.description

    module = SystemModule.query.filter(SystemModule.name.ilike(f"%{query}%")).first()
    if module:
        return module.description

    award = Award.query.filter(Award.title.ilike(f"%{query}%")).first()
    if award:
        return f"{award.title} - {award.date}: {award.category} at {award.location}. Description: {award.description}"

    return "Sorry, I couldn't understand your query."

if __name__ == '__main__':
    app.run(debug=True)

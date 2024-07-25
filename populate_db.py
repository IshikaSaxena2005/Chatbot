from app import db, Service

def populate_db():
    db.create_all()

    # Define new system modules and their descriptions
    new_modules = [
        ("Order & Payment Management System", "Order & Payment Management System: This module includes Work Order Management, Payment Management, and AMC Management."),
        ("Work Order Management", "Work Order Management: This module manages enquiries received, proposals, work orders, and tracking of work progress."),
        ("Payment Management", "Payment Management: It facilitates invoicing and tracking payments received from clients."),
        ("Survey Management System", "Survey Management System: Includes Survey Plan, Survey Form, and Survey Summary Report."),
        ("Survey Plan", "Survey Plan: Helps in planning and organizing surveys, defining objectives, and setting up survey parameters."),
        ("Survey Form", "Survey Form: Allows creation and management of survey forms for data collection."),
        ("Survey Summary Report", "Survey Summary Report: Generates reports summarizing the results and findings of surveys."),
        ("Vendor & Inventory Management System", "Vendor & Inventory Management System: Includes Vendor Management, Hardware Purchase Request, Billing Management, Hardware Stock & Inventory, and Hardware Indent."),
        ("Vendor Management", "Vendor Management: Maintains a database of vendors, their contact information, and transaction history."),
        ("Hardware Purchase Request", "Hardware Purchase Request: Allows users to request hardware or equipment purchases."),
        ("Resource Management System", "Resource Management System: Includes Attendance, DPR, Assigned Task, Field Visit, and Expenses."),
        ("Attendance", "Attendance: Tracks resource attendance and work hours."),
        ("DPR", "DPR (Daily Progress Report): Records daily progress on projects or tasks."),
        ("Assigned Task", "Assigned Task: Assigns tasks to team members and monitors their progress."),
        ("Support Ticketing System", "Support Ticketing System: Logs, tracks, and manages client support requests and issues."),
        ("Core Product Delivery", "Core Product Delivery: Delivers essential core products integral to the iCheckGate™ system."),
        ("Enterprise Offerings for iCheckGate™", "Enterprise Offerings: Includes enterprise-grade offerings designed to enhance iCheckGate™ capabilities."),
        ("Turnkey Solution", "Turnkey Solutio n: Includes end-to-end execution, commitment to maintenance, and full responsibility for implementation."),
        ("Awards & Recognition", "Awards & Recognition: Details about awards received by iCheckGate™, including Platinum Award, Gold Award, ET-DIGITECH Awards, and more.")
    ]

    for name, description in new_modules:
        existing_module = Service.query.filter_by(name=name).first()
        if not existing_module:
            new_module = Service(name=name, description=description)
            db.session.add(new_module)

    db.session.commit()

if __name__ == "__main__":
    populate_db()

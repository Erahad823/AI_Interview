import os
from dotenv import load_dotenv
import requests
import json

load_dotenv(override=True)

MODEL = os.environ['MODEL']
AUTH_KEY = os.environ['DEEPINFRAAPIKEY']
DEEPINFRA_URL = os.environ['URL_ENDPOINT']

headers = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {AUTH_KEY}'
}

def get_ai_response(prompt):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }
    response = requests.post(DEEPINFRA_URL, headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

def conduct_interview():


    resume = """
    Ravneet
    123 Tech Street, Silicon Valley, CA 94000
    johndoe@email.com | (555) 123-4567 | linkedin.com/in/johndoe

    SUMMARY
    Results-oriented DevOps Engineer with 7+ years of experience in system administration, automation, and continuous integration and deployment (CI/CD). Proficient in cloud infrastructure management, containerization, and scripting. Demonstrated ability to improve system performance and reliability through automation and best practices.

    SKILLS

    Languages: Python, Bash, Go, Ruby
    Tools & Technologies: Docker, Kubernetes, Jenkins, Terraform, Ansible, Git
    Cloud Platforms: AWS, Azure, Google Cloud Platform
    Operating Systems: Linux (Ubuntu, CentOS, Red Hat), Windows
    Monitoring & Logging: Prometheus, Grafana, ELK Stack
    Other: CI/CD, Infrastructure as Code (IaC), Configuration Management, Agile/Scrum
    PROFESSIONAL EXPERIENCE

    Senior DevOps Engineer | CloudTech Solutions | Jan 2020 - Present

    Architected and implemented a scalable, high-availability infrastructure on AWS using Terraform and Ansible.
    Improved deployment processes with Jenkins, reducing deployment time by 50%.
    Developed and maintained Docker images and Kubernetes clusters, enhancing application scalability and reliability.
    Automated monitoring and alerting using Prometheus and Grafana, resulting in a 30% decrease in incident response time.
    Collaborated with development teams to ensure seamless integration and deployment of applications.
    DevOps Engineer | DataSystems Inc. | Mar 2016 - Dec 2019

    Managed CI/CD pipelines using Jenkins and Git, ensuring reliable and consistent deployment processes.
    Implemented infrastructure as code using Terraform, reducing manual configuration efforts by 40%.
    Developed automated scripts in Python and Bash for system monitoring and maintenance.
    Configured and managed cloud infrastructure on Azure, optimizing resource utilization and cost.
    Monitored system performance and resolved issues proactively to minimize downtime.
    System Administrator | TechCorp | Jul 2013 - Feb 2016

    Administered Linux and Windows servers, ensuring high availability and security.
    Automated routine tasks using shell scripts, improving operational efficiency.
    Managed network infrastructure and troubleshooting issues to maintain network reliability.
    Implemented and maintained backup and disaster recovery solutions, ensuring data integrity.
    EDUCATION

    Bachelor of Science in Computer Science | University of California, Berkeley | 2009 - 2013

    CERTIFICATIONS

    AWS Certified DevOps Engineer - Professional
    Certified Kubernetes Administrator (CKA)
    Red Hat Certified Engineer (RHCE)
    PROJECTS

    CI/CD Pipeline for E-commerce Platform: Designed and implemented a CI/CD pipeline using Jenkins, Docker, and Kubernetes, resulting in faster and more reliable deployments.
    Infrastructure Automation: Automated the provisioning and configuration of cloud infrastructure using Terraform and Ansible, significantly reducing setup time and errors.
    Monitoring and Logging System: Set up a centralized monitoring and logging system with Prometheus and ELK Stack, improving system visibility and troubleshooting capabilities.
    PERSONAL PROJECTS

    Open-source Contributor: Contributed to various open-source projects on GitHub, including Kubernetes Helm charts and Jenkins shared libraries.
    DevOps Blog: Maintains a personal blog (devopsjohn.com) where he writes about DevOps practices, tools, and industry trends.

    """

    job_description = """
    Job Title: DevOps Engineer

    Company: InnovateTech Solutions

    Location: San Francisco, CA (Hybrid - 2 days in office, 3 days remote)

    About Us:
    InnovateTech Solutions is a fast-growing tech company specializing in developing innovative software solutions for various industries, including finance, healthcare, and e-commerce. We are committed to fostering a collaborative and dynamic work environment that encourages professional growth and creativity.

    Job Description:
    We are looking for a talented and experienced DevOps Engineer to join our dynamic team. The ideal candidate will have a strong background in system administration, automation, and continuous integration and deployment (CI/CD). As a DevOps Engineer, you will be responsible for managing and enhancing our cloud infrastructure, ensuring system reliability, and automating processes to improve efficiency.

    Responsibilities:

    Design, implement, and manage scalable and reliable cloud infrastructure using AWS, Azure, or Google Cloud Platform.
    Develop and maintain CI/CD pipelines using tools such as Jenkins, GitLab CI, or CircleCI.
    Containerize applications using Docker and orchestrate them with Kubernetes.
    Implement infrastructure as code (IaC) using Terraform, CloudFormation, or Ansible.
    Automate routine tasks and workflows using scripting languages such as Python, Bash, or Ruby.
    Monitor system performance and troubleshoot issues to ensure high availability and reliability.
    Collaborate with development, QA, and operations teams to ensure seamless integration and deployment of applications.
    Implement and maintain monitoring and logging solutions using tools such as Prometheus, Grafana, and the ELK Stack.
    Stay up-to-date with emerging technologies and industry trends, and apply this knowledge to improve existing systems and processes.
    Requirements:

    Bachelor's degree in Computer Science, Information Technology, or a related field.
    3+ years of experience as a DevOps Engineer or in a similar role.
    Strong proficiency in cloud platforms (AWS, Azure, or Google Cloud Platform).
    Experience with containerization and orchestration tools (Docker, Kubernetes).
    Proficiency in CI/CD tools (Jenkins, GitLab CI, CircleCI).
    Experience with infrastructure as code (Terraform, CloudFormation, Ansible).
    Strong scripting skills (Python, Bash, Ruby).
    Familiarity with monitoring and logging tools (Prometheus, Grafana, ELK Stack).
    Knowledge of version control systems (Git) and agile development methodologies.
    Excellent problem-solving skills and attention to detail.
    Strong communication and collaboration skills.
    Preferred Qualifications:

    AWS Certified DevOps Engineer or equivalent certification.
    Certified Kubernetes Administrator (CKA) or equivalent certification.
    Experience with configuration management tools (Chef, Puppet).
    Knowledge of security best practices and tools (Vault, Twistlock).
    Experience with serverless architecture and functions (AWS Lambda, Azure Functions).
    Benefits:

    Competitive salary and performance-based bonuses.
    Comprehensive health, dental, and vision insurance.
    401(k) plan with company match.
    Generous paid time off and holidays.
    Professional development opportunities and certifications.
    Flexible work hours and remote work options.
    Collaborative and inclusive work environment.
    How to Apply:
    Interested candidates are invited to submit their resume and a cover letter detailing their experience and qualifications to careers@innovatetechsolutions.com. Please include "DevOps Engineer Application" in the subject line.


    """

    initial_prompt = f"""
    Act as an Interviewer. Your task is to conduct an interview with a jobseeker based on their resume and the job description provided. Generate relevant questions one at a time. After each question, wait for the jobseeker's response before generating the next question.
    Generate Technical Question with difficulty level very high ask command and code.

    Resume:
    {resume}

    Job Description:
    {job_description}

    Generate and ask the first question.
    """

    responses = []
    conversation_history = initial_prompt

    for i in range(2):
        question = get_ai_response(conversation_history)
        print(f"\nQuestion {i+1}: {question}")
        answer = input("Your answer: ")
        responses.append({"question": question, "answer": answer})


    summary_prompt = f"""
    Carefully examine the Question asked by interviewer and answer by user then check thats the valid answer or not
    Summarize the following interview responses and provide an accuracy score out of 100% based on how well the candidate's answers align with the job requirements:

    {json.dumps(responses)}

    Resume:
    {resume}

    Job Description:
    {job_description}
    """

    summary = get_ai_response(summary_prompt)
    print("\nInterview Summary and Accuracy Score:")
    print(summary)

if __name__ == "__main__":
    conduct_interview()
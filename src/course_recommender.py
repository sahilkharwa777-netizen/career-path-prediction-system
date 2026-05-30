career_courses = {

    "Software Engineer": [
        "Python Programming",
        "Data Structures and Algorithms",
        "Object Oriented Programming",
        "System Design"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js"
    ],

    "Systems Security Administrator": [
        "Linux Administration",
        "Network Security",
        "Ethical Hacking",
        "Cyber Security Fundamentals",
        "CCNA"
    ],

    "Network Security Engineer": [
        "Cyber Security",
        "Ethical Hacking",
        "CCNA",
        "Penetration Testing"
    ],

    "Database Developer": [
        "SQL",
        "MySQL",
        "MongoDB",
        "Database Design"
    ],

    "UX Designer": [
        "UI/UX Design",
        "Figma",
        "Wireframing",
        "User Research"
    ]
}

def recommend_courses(career):
    return career_courses.get(
        career,
        ["No recommendations available"]
    )
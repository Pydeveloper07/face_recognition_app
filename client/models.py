import pathlib
lorem_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt " \
             "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco " \
             "laboris nisi ut aliquip ex ea commodo consequat."
video_file ='{}'.format(pathlib.Path().absolute()/"media/sample_video.mkv")



subject_list = [
    {
        "id": 0,
        "name": "Philosophy",
        "professor": "Kahramon Yakubov",
        "section": 3,
        "image": "img/philosophy.jpg",
        "video": video_file,
        "description": lorem_text,
        "content": 'Quite literally, the term "philosophy" means, "love of wisdom." In a broad sense, philosophy is '
                   'an activity people undertake when they seek to understand fundamental truths about themselves, '
                   'the world in which they live, and their relationships to the world and to each other. As an '
                   'academic discipline philosophy is much the same. Those who study philosophy are perpetually '
                   'engaged in asking, answering, and arguing for their answers to lifeâ€™s most basic questions. '
                   'To make such a pursuit more systematic academic philosophy is traditionally divided into major '
                   'areas of study.'
    },
    {
        "id": 1,
        "name": "Introduction to Economics",
        "professor": "Tongzon Jose",
        "section": 2,
        "image": "img/economics.jpg",
        "video": video_file,
        "description": lorem_text,
        "content": 'Economics can be defined in a few different ways. It’s the study of scarcity, the study of how '
                   'people use resources and respond to incentives, or the study of decision-making. It often involves '
                   'topics like wealth and finance, but it’s not all about money. Economics is a broad discipline that '
                   'helps us understand historical trends, interpret today’s headlines, and make predictions about the '
                   'coming years.'
    },
    {
        "id": 2,
        "name": "Operating System",
        "professor": "Abdul Rahim Naseer",
        "section": 3,
        "image": "img/os.jpg",
        "video": video_file,
        "description": lorem_text,
        "content": 'An operating system (OS) is system software that manages computer hardware, software resources, '
                   'and provides common services for computer programs. Time-sharing operating systems schedule '
                   'tasks for efficient use of the system and may also include accounting software for cost '
                   'allocation of processor time, mass storage, printing, and other resources. For hardware functions '
                   'such as input and output and memory allocation, the operating system acts as an intermediary '
                   'between programs and the computer hardware'
    },
    {
        "id": 3,
        "name": "Database",
        "professor": "Agostini Alessandro",
        "section": 2,
        "image": "img/db.jpg",
        "video": video_file,
        "description": lorem_text,
        "content": 'DBMS software primarily functions as an interface between the end user and the database, '
                   'simultaneously managing the data, the database engine, and the database schema in order to '
                   'facilitate the organization and manipulation of data. Though functions of DBMS vary greatly, '
                   'general-purpose DBMS features and capabilities should include: a user accessible catalog '
                   'describing metadata, DBMS library management system, data abstraction and independence, data '
                   'security, logging and auditing of activity, support for concurrency and transactions, support for '
                   'authorization of access, access support from remote locations, DBMS data recovery support in the '
                   'event of damage, and enforcement of constraints to ensure the data follows certain rules.'
    },
    {
        "id": 4,
        "name": "Computer Algorithm",
        "professor": "Seth Ashish",
        "section": 2,
        "image": "img/ca.jpg",
        "video": video_file,
        "description": lorem_text,
        "content": 'Consider how you use a computer in a typical day. For example, you start working on a report, '
                   'and once you have completed a paragraph, you perform a spell check. You open up a spreadsheet '
                   'application to do some financial projections to see if you can afford a new car loan. You use a '
                   'web browser to search online for a kind of car you want to buy. You may not think about this very '
                   'consciously, but all of these operations performed by your computer consist of algorithms. An '
                   'algorithm is a well-defined procedure that allows a computer to solve a problem. Another way to '
                   'describe an algorithm is a sequence of unambiguous instructions.'
    },
    {
        "id": 5,
        "name": "System Analysis",
        "professor": "Dragunov Andrei",
        "section": 3,
        "image": "img/sa.jpg",
        "video": video_file,
        "description": lorem_text,
        "content": 'System analysis is conducted for the purpose of studying a system or its parts in order to '
                   'identify its objectives. It is a problem solving technique that improves the system and ensures '
                   'that all the components of the system work efficiently to accomplish their purpose.'
    }
]
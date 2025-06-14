questions = [
    ["What is the capital of France?", "Paris", "London", "Rome", "Berlin", 1],
    
    ["What is the largest planet in our Solar System?", "Jupiter", "Saturn", "Earth", "Mars", 1],
    ["Who painted the ceiling of the Sistine Chapel?", "Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello", 2],
    ["What is the chemical symbol for water?", "H2O", "O2", "CO2", "HO", 1],
    ["Which continent is the Sahara Desert located on?", "Asia", "Africa", "Australia", "Europe", 2],
    ["Who invented the telephone?", "Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Isaac Newton", 3],
    ["What is the process by which plants make their food?", "Respiration", "Transpiration", "Photosynthesis", "Digestion", 3],
    ["Which animal is known as the 'King of the Jungle'?", "Tiger", "Lion", "Elephant", "Leopard", 2],
    ["Who is known as the father of computers?", "Albert Einstein", "Isaac Newton", "Charles Babbage", "Alan Turing", 3],
    ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Silver", 3],
    ["Which country is famous for the Carnival festival in Rio de Janeiro?", "Argentina", "Brazil", "Spain", "Italy", 2],
    ["What gas do humans need to breathe to survive?", "Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen", 1],
    ["Which language is spoken in Brazil?", "Spanish", "Portuguese", "French", "English", 2],
    ["What is the tallest mountain in the world?", "K2", "Mount Everest", "Kangchenjunga", "Makalu", 2],
    ["Which ocean is the largest?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["Which scientist proposed the three laws of motion?", "Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking", 1],
]
prizes=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,20000]
i=0
for question in questions:
    
    print(f"Question: {question[0]}")
    print(f"A.{question[1]}")
    print(f"B.{question[2]}")
    print(f"C.{question[3]}")
    print(f"D.{question[4]}")

    

    m=int(input("enter 1 for a, 2 for b,3 for c,4 for d "))
    
    if(question[5]==m):
        print("correct")
        
    else:
        print("incorrect")
        break
    print(f"you won {prizes[i]}")
    i+=1
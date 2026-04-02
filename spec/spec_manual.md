# Requirement ID: FR1 

- Description: [The app launch time shall not exceed 2 seconds on standard devices that application is designed to run on]
- Source Persona: [Daily driver user]
- Traceability: [Derived from review group G1]
- Acceptance Criteria: [Given the user is on a compatabile device When the user opens the application Then the application must be open and functioning within 2 seconds.]

# Requirement ID: FR2

- Description: [The system shall remember user preferences and last used settings]
- Source Persona: [Daily driver user]
- Traceability: [Derived from review group G1]
- Acceptance Criteria: [Given the user had previously changed UI settings for the chatbot When the user enters the chat in a new session Then the application must preserve the UI settings from the previous session.]

# Requirement ID: FR3

- Description: [Responses shall include at least one empathetic statement when negative sentiment is detected]
- Source Persona: [Human connection seeker user]
- Traceability: [Derived from review group G2]
- Acceptance Criteria: [Given the user sends a message expressing negative sentiment When the chatbot produces a response Then the response must include one statement that empathizes with the user.]

# Requirement ID: FR4

- Description: [The chatbot must provide an answer to all questions in any given user message, unless providing an answer compromises the user's safety in which case it must acknowledge the question and explain why it won't answer.]
- Source Persona: [Human connection seeker user]
- Traceability: [Derived from review group G2]
- Acceptance Criteria: [Given the user asks the chabot at least one question in a given message When the chatbot produces a response Then the chatbot must provide an answer to all questions and explanations for any quesitons it cannot answer.]

# Requirement ID: FR5

- Description: [App shall save all the user's conversations since account was created in an accessible form]
- Source Persona: [Analytical user]
- Traceability: [Derived from review group G3]
- Acceptance Criteria: [Given the user has had several conversations with the chatbot When the user logins to any given session Then the user shall be able to access any conversation since their account was created .]

# Requirement ID: FR6

- Description: [User shall be able to search past conversations and journal entries using keywords.]
- Source Persona: [Analytical user
- Traceability: [Derived from review group G3]
- Acceptance Criteria: [Given past conversation exist When the user enters a word in search of past conversations Then the application must display a representation of that conversation that can be read in full.]

# Requirement ID: FR7

- Description: [Users shall be able to adjust content complexity (simple vs detailed explanation)]
- Source Persona: [Neurodivergent user]
- Traceability: [Derived from review group G4]
- Acceptance Criteria: [Given the user wants to decrease complexity of application content When the user changes complexity to simple Then the application content will now use level B1 sentence structure and vocabulary according to Common European Framework of Reference for Languages.]

# Requirement ID: FR8

- Description: [Content shall include perspectives and language relevant to neurodivergent experiences.]
- Source Persona: [Neurodivergent user]
- Traceability: [Derived from review group G4]
- Acceptance Criteria: [Given the user acts the chatbot for mental health advice for neurodivergent people When the chatbot responds Then the response must reference directly/indirectly proven literature on mental health for neurodivergent people.]

# Requirement ID: FR9

- Description: [Animations shall be smooth and slow-paced, with no flashing or rapid movement.]
- Source Persona: [Stressed out user]
- Traceability: [Derived from review group G5]
- Acceptance Criteria: [Given the user is having conversation with the chatbot When the chatbot cartoon figure is moving Then pixel intensity of all pixel must not change color or intensity at a rate greater than 30 units per second on a scale of 255 units.]

# Requirement ID: FR10

- Description: [The system shall display no more than three options per screen.]
- Source Persona: [Stressed out user]
- Traceability: [Derived from review group G5]
- Acceptance Criteria: [Given the user is on any screen When the user is presented with options Then the application must present no more than 3 options.]

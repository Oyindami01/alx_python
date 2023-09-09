# PYTHON-OBJECT_RELATIONAL MAPPING

This repo is a collection of python scripts. It uses SQLAlchemy to interact with MySQL database.

### TABLE OF CONTENT

- Description
- Scripts
- Challenges
- Credits

#### DESCRIPTION
The scripts in this object_relational mapping is related to managing data in a MySQL database. We were provided with database and were asked to query such database.

#### SCRIPTS

1. 0-select_states.py
2. 1-filter_states.py
3. 2-my_filter_states.py
4. 3-my_safe_filter_states.py
5. 4-cities_by_state.py
6. model_state.py
7. 5-filter_cities.py
8. 7-model_state_fetch_all.py
9. 8-model_state_fetch_first.py
10. 9-model_state_filter_a.py

- **0-select_states.py:** This script lists all the states from the hbtn_0e_0_usa database

- **1-filter_states.py:** This script lists all states with a name starting with N (upper N) from the hbtn_0e_0_usa database.

- **2-my_filter_states.py:** This script takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

- **3-my_safe_filter_states:** This script lists states from the hbtn_0e_0_usa database based on search criteria.Here , we learn about sql injection and how to write our script in a way that is safe from injection.

- **4-cities_by_state.py:** This script lists all cities from the hbtn_0e_4_usa database by their states.

- **5-filter_cities.py:** This script lists all cities of a given state from the hbtn_0e_4_usa database.

- **model_state.py:** Here, we beign to make use of SQLAlchemy.; learning to trust the ORM magic. We make use of python classes too. This script is a module for defining a State class using SQLAlchemy.

- **7-model_state_fetch_all.py:** This script lists all State objects from the hbtn_0e_6_usa database but unlike we did earlier, we start to make use of python classes inheritance from the model_state.py.

- **8-model_state_fetch_first.py:** This script prints the first State object from the database hbtn_0e_6_usa.

- **9-model_state_filter_a.py:** This script lists all State objects that contain the letter 'a' in their name from the database hbtn_0e_6_usa. Like the 8 & 9, it also inherits from the model_states.py.

#### CHALLENGES

IN Script "4-cities_by_states", I had challenges trying Connect to the server using the context manager
also in script "9-model_state_filter_a", I had a challenge trying to close the session

#### CREDITS

Giving credit to @alx_africa, for giving us the project and giving us more projects to improve our software enginerring skills.

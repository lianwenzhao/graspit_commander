#!/usr/bin/env python
from graspit_commander import GraspitCommander
from graspit_interface.msg import SearchSpace, SearchEnergy,SearchContact

num_steps = 40010
GraspitCommander.loadWorld("test_planner")
GraspitCommander.planGrasps(max_steps=num_steps,
search_space=SearchSpace(SearchSpace.SPACE_COMPLETE),
#search_contact=SearchContact(SearchContact.CONTACT_LIVE),
search_energy=SearchEnergy(SearchEnergy.ENERGY_CONTACT));
#search_space=SearchSpace(SearchSpace.SPACE_AXIS_ANGLE),
#search_energy=SearchEnergy(SearchEnergy.ENERGY_AUTOGRASP_QUALITY));

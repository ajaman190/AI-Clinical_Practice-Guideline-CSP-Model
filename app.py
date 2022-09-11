from pywebio.input import *
from pywebio.output import *


domain = {"dyspnea": ["exertional","at rest","labored","No"],
          "beta_agonist": ["good response","partial response","weak response","no response","No"],
          "difficult_speech": ["absent","moderate","present","No"],
          "tachycardia": ["absent","present","No"],
          "tachypnea": ["exertional","at rest","labored","No"],
          "accessory_muscles": ["severe","moderate","none","No"],
          "breathing_sounds": ["normal","reduced","silent","No"],
          "typical_episode": ["better","same","worse","No"],
          "sao2": [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
          "pev": [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
          "fev": [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
         }
ndomain = {"dyspnea": [11,22,33,0],
          "beta_agonist": [11,22,33,33,0],
          "difficult_speech": [12,23,33,0],
          "tachycardia": [12,33,0],
          "tachypnea": [12,23,33,0],
          "accessory_muscles": [33,23,12,0],
          "breathing_sounds": [11,13,33,0],
          "typical_episode": [12,13,33,0],
          "sao2": [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
          "pev": [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
          "fev": [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
         }

"""Partial-Patient-Descriptor-Constraints (ppdc)"""
ppdc = {"dyspnea":{"DDS1":["exertional"],
                   "DDS2":["at rest"],
                   "DDS3":["labored"]
                  },
        "beta_agonist":{"DDS1":["good response"],
                        "DDS2":["partial response"],
                        "DDS3":["weak","no response"]
                       },
        "difficult_speech":{"DDS1":["absent"],
                            "DDS2":["absent","moderate"],
                            "DDS3":["moderate","present"]
                           },
        "tachycardia":{"DDS1":["absent"],
                       "DDS2":["absent"],
                       "DDS3":["present"]
                      },
        "tachypnea":{"DDS1":["exertional"],
                     "DDS2":["exertional","at rest"],
                     "DDS3":["at rest","labored"]
                    },
        "accessory_muscles":{"DDS1":["none"],
                             "DDS2":["none","moderate"],
                             "DDS3":["moderate","severe"]
                            },
        "breathing_sounds":{"DDS1":["normal","reduced"],
                            "DDS2":["reduced"],
                            "DDS3":["reduced","silent"]
                           },
        "typical_episode":{"DDS1":["better","same"],
                           "DDS2":["same","worse"],
                           "DDS3":["same","worse"]
                          },
        "sao2":{"DDS1":[96,97,98,99,100],
                "DDS2":[76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
                "DDS3":[76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
               },
        "pev":{"DDS1":[92,93,94,95],
               "DDS2":[51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75],
               "DDS3":[51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
              },
        "fev":{"DDS1":[80,81,82,83,84,85,86,87,88,89,90,91],
               "DDS2":[40,41,42,43,44,45,46,47,48,49,50],
               "DDS3":[40,41,42,43,44,45,46,47,48,49,50]
              }
        }

"""Complete-Patient-Descriptor-Constraint (cpdc)"""
cpdc = {"DDS1" :{"dyspnea":["exertional"],"beta_agonist":["good response"],"difficult_speech":["absent"],"tachycardia":["absent"],"tachypnea":["exertional"],"accessory_muscles":["none"],"breathing_sounds": ["normal","reduced"],"typical_episode": ["better","same"],"sao2":[96,97,98,99,100],"pev": [76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"fev": [76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]},
        "DDS2" :{"dyspnea":["at rest"],"beta_agonist":["partial response"],"difficult_speech":["absent","moderate"],"tachycardia":["absent"],"tachypnea":["exertional","at rest"],"accessory_muscles":["none","moderate"],"breathing_sounds": ["reduced"],"typical_episode": ["same","worse"],"sao2":[92,93,94,95],"pev": [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75],"fev": [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]},
        "DDS3" :{"dyspnea":["labored"],"beta_agonist":["weak","no response"],"difficult_speech":["moderate","present"],"tachycardia":["present"],"tachypnea":["at rest","labored"],"accessory_muscles":["moderate","severe"],"breathing_sounds": ["reduced","silent"],"typical_episode": ["same","worse"],"sao2":[80,81,82,83,84,85,86,87,88,89,90,91],"pev": [40,41,42,43,44,45,46,47,48,49,50],"fev": [40,41,42,43,44,45,46,47,48,49,50]},
       }

"""Encoded cpdc attribute values to numeric values"""
ncpdc = {"DDS1" :{"dyspnea":[11],"beta_agonist":[11],"difficult_speech":[12],"tachycardia":[12],"tachypnea":[12],"accessory_muscles":[12],"breathing_sounds": [11,13],"typical_episode": [11,13],"sao2":[96,97,98,99,100],"pev": [76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],"fev": [76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]},
        "DDS2" :{"dyspnea":[22],"beta_agonist":[22],"difficult_speech":[12,23],"tachycardia":[12],"tachypnea":[12,23],"accessory_muscles":[12,23],"breathing_sounds": [13],"typical_episode": [13,23],"sao2":[92,93,94,95],"pev": [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75],"fev": [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]},
        "DDS3" :{"dyspnea":[33],"beta_agonist":[33,33],"difficult_speech":[23,33],"tachycardia":[33],"tachypnea":[23,33],"accessory_muscles":[23,33],"breathing_sounds": [13,33],"typical_episode": [13,23],"sao2":[80,81,82,83,84,85,86,87,88,89,90,91],"pev": [40,41,42,43,44,45,46,47,48,49,50],"fev": [40,41,42,43,44,45,46,47,48,49,50]},
       }

"""Pediatric Asthma CPG input"""
class CPGInput:
  
  def __init__(self,data,state):
    self.att = data
    if state == "mild":
      self.state = "DDS1"
    elif state == "moderate":
      self.state = "DDS2"
    elif state == "severe":
      self.state = "DDS3"
    
  def add(self):
    attributes = domain.keys()
    for attribute in attributes:
      print(attribute," : ",domain[attribute])
      self.key = attribute
      self.value = input("Enter :") 
      self.att[self.key] = self.value
      print("\n")

    state = input()
    if state == "mild":
      self.state = "DDS1"
    elif state == "moderate":
      self.state = "DDS2"
    elif state == "severe":
      self.state = "DDS3"

"""Node consistency check on incomplete input solution -"""
def check1(pstate):
  flag = []
  cnt = 0
  attributes = domain.keys()
  state = pstate.state

  for attribute in attributes:
    if pstate.att[attribute] == "No" or pstate.att[attribute] == "no" or pstate.att[attribute] == "NO":
      flag.append(0)

    else:
      cnt = cnt+1
      present = False
      for value in ppdc[attribute][state]:
        if pstate.att[attribute] == value :
          present = True

      if present:
        flag.append(2) 

      else:
        flag.append(1)  
  
  if cnt == flag.count(1):
    put_text("All data entered is inconsistent for the confirmed diagnosis.")
  else:
    check2(pstate,flag)

"""Incomplete solution to complete solution -"""
def check2(pstate,flag):
  state = pstate.state

  if flag.count(1) == 0:
    attributes = list(domain.keys())
    for (conflict,attribute) in zip(flag,attributes):
      if conflict == 0:
        index = ncpdc[state][attribute].index(min(ncpdc[state][attribute]))
        pstate.att[attribute] = cpdc[state][attribute][index]
  
  else:
    attributes = list(domain.keys())
    for (conflict,attribute) in zip(flag,attributes):
      if conflict == 1:
        value = mineuclideandist(pstate,attribute,pstate.att[attribute])
        pstate.att[attribute] = value
        
      elif conflict == 0:
        if state == 'DDS1':
          if attribute == 'sao2' or attribute == 'pev' or attribute == 'fev':
            index = ncpdc[state][attribute].index(min(ncpdc[state][attribute]))
            pstate.att[attribute] = cpdc[state][attribute][index]
          else:
            index = ncpdc[state][attribute].index(max(ncpdc[state][attribute]))
            pstate.att[attribute] = cpdc[state][attribute][index]

        elif state == 'DDS3' or state == 'DDS2':
          if attribute == 'sao2' or attribute == 'pev' or attribute == 'fev':
            index = ncpdc[state][attribute].index(max(ncpdc[state][attribute]))
            pstate.att[attribute] = cpdc[state][attribute][index]
          else:
            index = ncpdc[state][attribute].index(min(ncpdc[state][attribute]))
            pstate.att[attribute] = cpdc[state][attribute][index]

  solution(pstate,flag)

def mineuclideandist(pstate,attribute,conflict):
  state = pstate.state
  nconflict = ndomain[attribute][domain[attribute].index(conflict)]
  similarity = []
  
  constraintlist = ncpdc[state][attribute]
  for constraint in constraintlist:
    distance = euclideandist(constraint,nconflict)
    similarity.append(distance)

  index = similarity.index(min(similarity))
  return cpdc[state][attribute][index]  

from math import sqrt

def euclideandist(x,y):
  distance = sqrt((x-y)**2)
  return distance

def solution(pstate,flag):
  
  put_markdown("""#
  
  Output:""")
  printdiagnosis(pstate)

  if flag.count(1) == 0:
    put_text("All data entered is Consistent for the confirmed diagnosis.")
  else:
    put_markdown("%d data entered is Inconsistent for the confirmed diagnosis."%(flag.count(1)))
  
  put_markdown("Patient is in %s stage of pediatric asthma."%(printstate(pstate)))

def printdiagnosis(pstate):
    put_markdown(("""
    
    |                      | %s          | 
    | -------------------- | ------------- |
    | Dyspnea              | %s          | 
    | Beta Agonist         | %s          | 
    | Difficult Speech     | %s          | 
    | Tachycardia          | %s          | 
    | Tachypnea            | %s          | 
    | Accessory muscles    | %s          |
    | Breathing sounds     | %s          | 
    | Typical episode      | %s          | 
    | SaO2                 | %s          | 
    | PEV                  | %s          | 
    | FEV                  | %s          | 
    
    """%(printstate(pstate),pstate.att['dyspnea'],pstate.att['beta_agonist'],pstate.att['difficult_speech'],pstate.att['tachycardia'],pstate.att['tachypnea'],pstate.att['accessory_muscles'],pstate.att['breathing_sounds'],pstate.att['typical_episode'],pstate.att['sao2'],pstate.att['pev'],pstate.att['fev'])), strip_indent=4)


def printstate(pstate):
  if pstate.state == "DDS1":
    return "mild"
  elif pstate.state == "DDS2":
    return "moderate"
  elif pstate.state == "DDS3":
    return "severe"


def cpg():

    put_markdown(("""# Clinical Practice Guidelines
    
    [Clinical Practice Guidelines](https://www.ncbi.nlm.nih.gov/books/NBK390308/) (CPG) are recommendations on how to diagnose and treat a medical condition. They are mainly written for doctors. 
    
    CPG Model for Pediatric Asthma:
    
    |                      | Mild          | Moderate      | Severe        |
    | -------------------- | ------------- | ------------- | ------------- |
    | Dyspnea              | exertional    | at rest       | labored       |
    | Beta Agonist         | good response | partial response| weak or no response|
    | Difficult Speech     | absent        | absent or moderate| moderate or present|
    | Tachycardia          | absent        | absent        | present       |
    | Tachypnea            | exertional    | exertional or at rest| at rest or labored|
    | Accessory muscles    | none          | none or moderate| moderate or severe|
    | Breathing sounds     | normal or reduced| reduced    | reduced or silent|
    | Typical episode      | better or same| same or worse | same or worse |
    | SaO2                 | >95           | 92-95         | <92           |
    | PEV                  | >75           | 50-75         | <50           |
    | FEV                  | >75           | 50-75         | <50           |
    
    """), strip_indent=4)

    data = input_group('Fill the Present Patient State Diagnosis Result',[
        select('Dyspnea:',domain['dyspnea'], name='dyspnea'),
        select('Beta Agonist:',domain['beta_agonist'], name='beta_agonist'),
        select('Difficult Speech:',domain['difficult_speech'], name='difficult_speech'),
        select('Tachycardia:',domain['tachycardia'], name='tachycardia'),
        select('Tachypnea:',domain['tachypnea'], name='tachypnea'),
        select('Accessory Muscles:',domain['accessory_muscles'], name='accessory_muscles'),
        select('Breathing Sounds:',domain['breathing_sounds'], name='breathing_sounds'),
        select('Typical Episode:',domain['typical_episode'], name='typical_episode'),
        input('SaO2: (Enter in b/w 80-100 or No)', name='sao2', type=TEXT),
        input('PEV: (Enter in b/w 40-100 or No)', name='pev', type=TEXT),
        input('FEV: (Enter in b/w 40-100 or No)', name='fev', type=TEXT)
    ])
    if data['sao2'] != 'No':
        data['sao2']= int(data['sao2'])
    if data['pev'] != 'No':
        data['pev']= int(data['pev'])
    if data['fev'] != 'No':
        data['fev']= int(data['fev'])

    info = input_group(('Fill the Present Asthma Stage (only for Physician)'), [
        select('Select',['mild','moderate','severe'], name='state')
    ])

    pstate = CPGInput(data,info['state'])
    put_markdown("""#

    Input:""")
    printdiagnosis(pstate)
    put_text("\n")
    check1(pstate)

if __name__ == '__main__':
    cpg()
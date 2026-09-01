from deepeval.red_teaming import RedTeamer
from deepeval.red_teaming import AttackEnhancement, Vulnerability
from hal import Hal

hal = Hal()

red_teamer=RedTeamer(
    target_purpose=hal.get_system_purpose(),
    target_system_prompt=hal.get_system_prompt(),
    synthesizer_model="gpt-3.5-turbo-0125",
    evaluation_model="gpt4o",
    async_mode=True
)

results = red_teamer.scan(
   target_model=hal,
   attacks_per_vulnerability=5,
   vulnerabilities=[
      Vulnerability.PII_API_DB,
      Vulnerability.PII_DIRECT,
      Vulnerability.PII_SESSION,
      Vulnerability.DATA_LEAKAGE,
      Vulnerability.PRIVACY,
   ],
   attack_enhancements={
      AttackEnhancement.BASE64: 0.25,
      AttackEnhancement.GRAY_BOX_ATTACK: 0.25,
      AttackEnhancement.JAILBREAK_CRESCENDO: 0.25,
      AttackEnhancement.MULTILINGUAL: 0.25,
   }
)
print(results) 

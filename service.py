import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService

load_dotenv()

api_key = os.getenv("QUANTUM_API_KEY")
crn = os.getenv("CRN_INSTANCE")

# Quick sanity checks (don't print the whole key)
print("api_key present:", bool(api_key), "len:", len(api_key) if api_key else None, "repr head:", repr(api_key[:6]) if api_key else None)
print("crn present:", bool(crn), "repr head:", repr(crn[:20]) if crn else None)

# If you ever saved a bad account before, clear it so Qiskit doesn't reuse it.
try:
    QiskitRuntimeService.delete_account()
except Exception:
    pass

QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",   # important: makes Qiskit use IBM Cloud/IAM flow
    token=api_key.strip() if api_key else None,
    instance=crn.strip() if crn else None,
    overwrite=True,
    set_as_default=True,
)

service = QiskitRuntimeService()
print("Authenticated. Instances:", len(service.instances()))
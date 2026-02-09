import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService

load_dotenv()

QiskitRuntimeService.save_account(
    token=os.getenv("QUANTUM_API_KEY"),
    instance=os.getenv("CRN_INSTANCE")
)
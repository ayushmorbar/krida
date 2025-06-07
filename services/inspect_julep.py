# inspect_julep.py
# A diagnostic script to determine the correct methods in the Julep SDK.

import os
try:
    from julep import Julep
except ImportError:
    print("FATAL ERROR: The 'julep-ai' library is not installed or not found in this environment.")
    print("Please run 'pip install julep-ai' and try again.")
    exit()

print("--- Julep SDK Inspection Report ---")

# Use a dummy key for inspection; no real API calls will be made.
api_key = os.getenv('JULEP_API_KEY', 'dummy_key_for_inspection')

try:
    client = Julep(api_key=api_key)
    print("Successfully created a Julep client object.")
    print("-" * 20)

    # --- Inspect the top-level client object ---
    print("\n[1] Methods and attributes available directly on the 'client' object:")
    client_attributes = [attr for attr in dir(client) if not attr.startswith('_')]
    print(client_attributes)

    # --- Dig deeper into the 'agents' resource, if it exists ---
    print("\n[2] Inspecting 'client.agents' resource...")
    if hasattr(client, 'agents'):
        print("  - Found 'client.agents'. Available methods:")
        agent_methods = [attr for attr in dir(client.agents) if not attr.startswith('_')]
        print(f"    {agent_methods}")
    else:
        print("  - 'client.agents' NOT FOUND.")

    # --- Dig deeper into the 'sessions' resource, if it exists ---
    print("\n[3] Inspecting 'client.sessions' resource...")
    if hasattr(client, 'sessions'):
        print("  - Found 'client.sessions'. Available methods:")
        session_methods = [attr for attr in dir(client.sessions) if not attr.startswith('_')]
        print(f"    {session_methods}")
    else:
        print("  - 'client.sessions' NOT FOUND.")
        
    print("\n--- Inspection Complete ---")
    print("\nPlease copy and paste this entire report. It will show us the correct path forward.")

except Exception as e:
    print(f"\nAn unexpected error occurred during inspection: {e}")


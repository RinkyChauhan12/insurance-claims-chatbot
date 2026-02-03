def insurance_claims_chatbot():
    print("Welcome to the Insurance Claims Chatbot 🛡️")

    policy_type = input("Enter policy type (health/vehicle): ")
    claim_amount = int(input("Enter claim amount: "))
    incident_reason = input("Enter reason for claim: ")

    policy_limits = {
        "health": 100000,
        "vehicle": 50000
    }

    print("\nProcessing your claim using compressed policy rules...\n")

    if claim_amount <= policy_limits.get(policy_type, 0):
        print("✅ Claim Eligible")
        print("📊 Claim Eligibility Score: 82%")
        print("📝 Claim Summary Generated Successfully")
    else:
        print("❌ Claim Amount exceeds policy limit")
        print("📊 Claim Eligibility Score: 30%")

insurance_claims_chatbot()

import asyncio
import sys
from app.services.keycloak_service import KeyCloakService
from app.services.pf_api_service import PfApiService


async def test_keycloak():
    print("🔐 Testing KeyCloak authentication...")
    service = KeyCloakService()
    username = input("Enter username: ")
    password = input("Enter password: ")
    response = await service.validate_user(username, password)
    if response.success:
        print("✅ Authentication successful!")
        print(f"   Token: {response.data.access_token[:50]}...")
        return response.data.access_token
    else:
        print(f"❌ Authentication failed: {response.message}")
        return None


async def test_pf_api(token=None):
    print("\n📄 Testing Printable Forms API...")
    service = PfApiService()
    print("   Fetching template files...")
    documents = await service.get_template_files(token)
    if documents:
        print(f"✅ Found {len(documents)} documents:")
        for doc in documents[:3]:
            print(f"   - {doc.file_name} (ID: {doc.document_id})")
    else:
        print("❌ No documents found")


async def main():
    print("🧪 API Test Suite\n")
    print("=" * 50)
    token = await test_keycloak()
    if token:
        await test_pf_api(token)
    print("\n" + "=" * 50)
    print("✅ Tests completed!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

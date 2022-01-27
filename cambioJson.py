bits = {"bits/adf_devsecops": "1.2.4",
        "bits/adf_simple_auth": "1.3.8",
        "bits/express_auth": "1.0.9",
        "bits/aws_service": "1.1.0",
        "bits/oneapp": "1.6.8",
        "bits/oneapp_adminimal": "1.0.0",
        "bits/oneapp_convergent": "2.2.2",
        "bits/oneapp_home": "1.4.14",
        "bits/oneapp_mobile": "2.3.27"}

bits2 = {"bits/adf_devsecops": "1.2.6",#modify
        "bits/adf_simple_auth": "1.3.9",
        "bits/express_auth": "1.0.9",
        "bits/aws_service": "1.1.2",#modify
        "bits/oneapp": "1.6.8",
        "bits/oneapp_adminimal": "1.0.0",
        "bits/oneapp_convergent": "2.2.2",
        "bits/oneapp_home": "1.4.14",
        "bits/oneapp_mobile": "2.3.27"}

print(bits)
print("\n================================================================\n")
print(bits2)
print("\n================================================================\n")
bits.update(bits2)
print(bits)

# for b in bits:
#     k = b
#     v = bits[b]
#     #print(f"{k} : {v}")
    
    
#     for b2 in bits2:
#         k2 = b2
#         v2 = bits2[b]
#         #print(f"{k2} : {v2}")
        
#         if k == k2 and v != v2:
#             print(f"diferente {v} = {v2}")
#             v = v2
#             bits.update({k : v})
#             print(f"nuevo {v} = {v2}")
#         # else:
#         #     print(f"igual {v} = {v2}")
            
# print("===============================")
# for b in bits:
#     k = b
#     v = bits[b]
#     print(f"{k} : {v}")
            
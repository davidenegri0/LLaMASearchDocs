import requests

abstract = "Web applications have been increasingly deployed on the Internet. How to effectively allocate system resources to meet the Service Level Objectives (SLOs) is a challenging problem for Web application providers. In this article, we propose a scheme for automated performance control of Web applications via dynamic resource allocations. The scheme uses a queueing model predictor and an online adaptive feedback loop that enforces admission control of the incoming requests to ensure the desired response time target is met. The proposed Queueing-Model-Based Adaptive Control approach combines both the modeling power of queueing theory and the self-tuning power of adaptive control. Therefore, it can handle both modeling inaccuracies and load disturbances in a better way. To evaluate the proposed approach, we built a multi-tiered Web application testbed with open-source components widely adopted in industry. Experimental studies conducted on the testbed demonstrated the effectiveness of the proposed scheme"

to_send = abstract.replace(' ', '_')

response = requests.get(f"http://localhost:5000/search/1/{to_send}")

print(response.content.decode())
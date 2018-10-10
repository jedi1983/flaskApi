import unittest
import requests
import json
import sys
import time

class NewsTest(unittest.TestCase):

	def testStatusData(self):
		data = {"statuscode": "draft"}
		resp = requests.post('http://localhost:5000/api/v1/Status',json=data)
		self.assertEqual(resp.status_code, 201)
		self.assertIn('draft',str(resp.json()['data']))
		resp = requests.get('http://localhost:5000/api/v1/Status')
		self.assertEqual(resp.status_code,200)
		self.assertIn('draft',str(resp.json()['data']))
		data = {"id": 1,"statuscode": "test"}
		resp = requests.put('http://localhost:5000/api/v1/Status',json=data)
		self.assertEqual(resp.status_code, 204)
		data = {"id": 1}
		resp = requests.delete('http://localhost:5000/api/v1/Status',json=data)
		self.assertEqual(resp.status_code, 204)

	def testTopicsData(self):
		data = {"topicname": "politik"}
		resp = requests.post('http://localhost:5000/api/v1/Topic',json=data)
		self.assertEqual(resp.status_code, 201)
		self.assertIn('politik',str(resp.json()['data']))
		resp = requests.get('http://localhost:5000/api/v1/Topic')
		self.assertEqual(resp.status_code,200)
		self.assertIn('politik',str(resp.json()['data']))
		data = {"id": 1,"topicname": "KPU"}
		resp = requests.put('http://localhost:5000/api/v1/Topic',json=data)
		self.assertEqual(resp.status_code, 204)
		data = {"id": 1}
		resp = requests.delete('http://localhost:5000/api/v1/Topic',json=data)
		self.assertEqual(resp.status_code, 204)

	def testNewsData(self):
		data = {"title": "Ratna Sarumpaet", "article": "This is A Stub Article", "status": 1}
		resp = requests.post('http://localhost:5000/api/v1/News',json=data)
		self.assertEqual(resp.status_code, 201)
		self.assertIn('Ratna Sarumpaet',str(resp.json()['data']))
		resp = requests.get('http://localhost:5000/api/v1/News')
		self.assertEqual(resp.status_code,200)
		self.assertIn('Ratna Sarumpaet',str(resp.json()['data']))
		data = {"id": 1,"title": "Ratna Sarumpaet V2", "article": "This is a stub v1","status":1}
		resp = requests.put('http://localhost:5000/api/v1/News',json=data)
		self.assertEqual(resp.status_code, 204)
		data = {"id": 1,"title": "Ratna Sarumpaet V2", "article": "This is a stub v1","status":1}
		resp = requests.delete('http://localhost:5000/api/v1/News',json=data)
		self.assertEqual(resp.status_code, 204)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
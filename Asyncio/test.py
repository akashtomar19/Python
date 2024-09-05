import asyncio 
 
def demo_function(i): 
	asyncio.sleep(1) 
	print(f"Hello {i}") 
 
def main(): 
	# tasks = [ 
	# demo_function(i) for i in range(0, 100) 
    # ] 
	for i in range(0, 100):
		demo_function(i)
	# await asyncio.gather(*tasks) 
	
main()
 
# asyncio.run(main())

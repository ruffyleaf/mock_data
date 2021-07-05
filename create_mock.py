#fruits = ['durian', 'mangosteen', 'mango', 'orange', 'apple', 'pear', 'jackfruit']
#print(random.sample(fruits, random.randint(1, len(fruits))))

from OrderGenerator import ProductGenerator

def main():
    fruits = ['durian', 'mangosteen', 'mango', 'orange', 'apple', 'pear', 'jackfruit']

    with open('out.csv', 'w') as f:
        f.write('order_id, item, quantity\n')
        for i in range(100):
            pg = ProductGenerator(fruits)
            pg.create_order_id()
            f.write(str(pg.order_id) + ','+ pg.fruit + ',' + str(pg.quantity) + '\n')        

if __name__ == "__main__":
    # execute only if run as a script
    main()

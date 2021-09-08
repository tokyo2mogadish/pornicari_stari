import simplegui

A = [ 0, 1, 0, 1, 0, 1, 0]

print '***************************'
def PassingCars(A):    
    right = 0
    left = 0
    for i in A:
        if i == 0: # the car is going east
            right += 1
        else: # the car is going west
            left += right
    return left if left <= 1000000000 else -1

print 'solution: ', PassingCars(A)

print '----PassingCars C#----'

# class Program
#    {
#        static void Main(string[] args)
#        {
#            int[] A = new int[] { 0, 1, 0, 1, 0, 1, 0 };

#            //Console.WriteLine(MaxCounters(N, A).ToString());
#            Console.WriteLine("{0}", string.Join(", ", PassingCars(A)));
#            Console.ReadLine();
#        }
#
#        public static int PassingCars(int[] A)
#        {
#            int right = 0;
#            int left = 0;
#            foreach (int item in A)
#            {
#                if (item == 0)
#                {
#                    right += 1;
#                }
#                else
#                {
#                    left += right;
#                }
#            }
#            if (left <= 1000000000)
#            {
#                return left;
#            }
#            else return -1;
#        }
#    }
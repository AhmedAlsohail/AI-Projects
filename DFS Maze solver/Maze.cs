using System;
using System.Collections.Generic;

namespace Maze
{
    class main
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.White;

            int[,] maze =
{
                {1, 1, 1, 1, 1},
                {1, 2, 0, 1, 1},
                {1, 1, 0, 1, 1},
                {0, 0, 0, 0, 0},
                {0, 1, 1, 1, 3}

            /*
             above is the maze,

            integer 0 represents the places we can move in.
            integer 1 represents walls
            integer 2 is the starting point ("a maze can not have more than One Starting Point").
            integer 3 is the Exit ("A maze can have more than One Exit, and the Exit can be anywhere on the maze").
            */
            };

            int[,] maze2 =
{
                {1, 1, 1, 1, 1, 1},
                {1, 2, 0, 1, 1, 1},
                {1, 1, 0, 1, 1, 0},
                {0, 0, 0, 0, 0, 0},
                {0, 1, 1, 1, 3, 1},
                {0, 0, 0, 0, 0, 0},
            };

            SolveMaze(maze2);
        }

        public static void SolveMaze(int[,] maze)
        {
            if(maze is null || maze.Length == 0)
            {
                Console.WriteLine("Invalid, Null or Empty maze.");
                return;
            }
            // 2d matrix of Vertices, contain the same maze but as a Vertices instead of integers.
            Vertex[,] VertexMaze = new Vertex[maze.GetLength(0), maze.GetLength(1)];
            // list contain the attributes of the maze taht we can move in.
            List<Vertex> mazeList = new List<Vertex>();
            // the starting point.
            Vertex root = null;

            //will be used to help printing the maze.
            int biggestNum = maze.GetLength(0) * maze.GetLength(1);
            //to know what numerical value our maximum number is in (1, 10, 100, 1000, 10000, etc..).
            int biggestNumLen = (int)Math.Pow(10, biggestNum.ToString().Length - 1);


            // Nested loop, to go through the whole matrix.
            for (int i = 0; i < maze.GetLength(1); i++)
            {
                Console.WriteLine("");
                for (int j = 0; j < maze.GetLength(0); j++)
                {
                    // check we have no Attribute with Unkown Integer, if it is found stop the execution.
                    if (maze[i, j] > 3 || maze[i, j] < 0)
                    {
                        Console.Write("\n\nInvalid Maze, Attribute with Unkown Integer: \"" + maze[i, j] + "\"");
                        System.Environment.Exit(0);
                    }

                    // make vertex attribue out of the interger attibute Form "Maze" Matrix, giving it the same coordinates,
                    // the name is based on attributes Numeric Order (1, 2, 3 ,4, etc..).
                    VertexMaze[i, j] = new Vertex((j + 1 + i * 5).ToString());

                    // set the type of the Vertex (0, 1, 2, or 3).
                    VertexMaze[i, j].settype(maze[i, j]);

                    //set the coocoordinates, these two will be used around line 110 when setting the neighbors.
                    // Set the Horizontal coordinate.
                    VertexMaze[i, j].setX(i);
                    // Set the Vertical coordinate. 
                    VertexMaze[i, j].setY(j);

                    // Print the maze.
                    if ((j + 1 + i * 5) < biggestNumLen)
                        Console.Write(" ");
                    Console.Write(VertexMaze[i, j] + " ");

                    // Check if this a Starting Point
                    if (maze[i, j] == 2)
                    {
                        // Check if there was another Starting Point, if there was then stop the execution.
                        if (!(root is null))
                        {
                            Console.WriteLine("\n");
                            Console.Write("\n\nInvalid Maze, More than One Starting Point");
                            System.Environment.Exit(0);
                        }

                        //make this Vertex the root, and add the it to List as the first element.
                        root = VertexMaze[i, j];
                        mazeList.Insert(0, VertexMaze[i, j]);
                    }
                    // if it was not a Starting Point, Check if it is a wall or not, if it is not then add the vertex to the List.
                    else if (maze[i, j] != 1)
                        mazeList.Add(VertexMaze[i, j]);
                }
            }

            // Now after We have checked every element, there is a chance we have not seen any type 2 (Starting Point), so we have to check it,
            // if there was not then stop the execution.
            if (root is null)
            {
                Console.WriteLine("\n");
                Console.Write("\nInvalid Maze, No Starting Point");
                System.Environment.Exit(0);
            }

            // We need the tell each Vertex who are his neighbors, this it to help "DFS" method to move between the Vertices without problems. 
            // go Through the "mazeList" to assign the nieghbors to each vertex,
            // the elements of type 1 (Walls) will not be considerd as neigbors.
            foreach (Vertex v in mazeList)
            {
                if ((v.getX() < maze.GetLength(1) - 1) && (VertexMaze[v.getX() + 1, v.getY()].gettype() != 1))
                    v.addNeighbors(VertexMaze[v.getX() + 1, v.getY()]);

                if ((v.getX() > 0) && (VertexMaze[v.getX() - 1, v.getY()].gettype() != 1))
                    v.addNeighbors(VertexMaze[v.getX() - 1, v.getY()]);

                if ((v.getY() < maze.GetLength(0) - 1) && (VertexMaze[v.getX(), v.getY() + 1].gettype() != 1))
                    v.addNeighbors(VertexMaze[v.getX(), v.getY() + 1]);

                if ((v.getY() > 0) && (VertexMaze[v.getX(), v.getY() - 1].gettype() != 1))
                    v.addNeighbors(VertexMaze[v.getX(), v.getY() - 1]);
            }

            // make new object of class "DFS_stack_maze_Version", then find and print the path using "DFS_SolveMaze" method.
            Console.WriteLine("\n");
            DFS_stack_maze_Version DFS = new DFS_stack_maze_Version();
            DFS.DFS_SolveMaze(root);
        }
    }

    class DFS_stack_maze_Version
    {
        // The DFS Algorithm Uses the "LIFO" structure or Stack (LAST IN FIRST OUT).
        private Stack<Vertex> mystack = new Stack<Vertex>();

        // List contaiting the path, the path from starting point to the Exit is stored here to be printed at the end.
        private List<Vertex> path = new List<Vertex>();

        // A backUp List, Used when we might need to backtrack.
        private List<Vertex> backUpPath = new List<Vertex>();

        // Store the last Vertex we visited in this Vertex.
        private Vertex previous;

        public void DFS_SolveMaze(Vertex rootVertex)
        {
            // Push the root to the stack and set it as visited.
            mystack.Push(rootVertex);
            rootVertex.setVisited(true);

            // while the stack is not empty.
            while (mystack.Count > 0)
            {
                // Pop the last elemnt from the stack.
                Vertex currentVertex = mystack.Pop();

                // Check if we need to load the backUp or not using "needBackup" metod.
                // if getBackUp was still set to true then we need to load the back up the the original path.
                if (ShouldBackup(currentVertex) && (backUpPath != null))
                    path = new List<Vertex>(backUpPath);

                // Check if this Vertex is the Exit then:
                if (currentVertex.gettype() == 3)
                {
                    // Print the path, this does not include the Exit.
                    printPath(path);
                    // Change the font Color to give the Exit unique Color.
                    Console.ForegroundColor = ConsoleColor.Green;
                    // Finally Print the exit.
                    Console.WriteLine(currentVertex);
                    // return to the old font color.
                    Console.ForegroundColor = ConsoleColor.White;
                    // Stop The execution.
                    System.Environment.Exit(0);
                }

                // Add the current Vertex to the path.
                path.Add(currentVertex);

                // if the current Vertex have more than 1 Unvisitd Neighbors then we need to take a backUp.
                // First check the number of all neighbors, if it is more than 1 then check the number of unvisited neighbors.
                if (currentVertex.getNeighbors().Count > 1)
                {
                    // Count the number of the Unvisited Neighbors.
                    int UnvisitedNeighbors = 0;
                    foreach (Vertex v in currentVertex.getNeighbors())
                    {
                        if (!v.getVisited())
                            UnvisitedNeighbors++;
                    }

                    // if it is more than 1 then take the backUp.
                    if(UnvisitedNeighbors > 1)
                        backUpPath = new List<Vertex>(path);
                }

                // Now we are finished working on this Vertex, set it as the Previous to be used in next Vertex.
                previous = currentVertex;

                // Now go to next Vertex with DFS algorithm.
                foreach (Vertex v in currentVertex.getNeighbors())
                {
                    if (!v.getVisited())
                    {
                        v.setVisited(true);
                        mystack.Push(v);
                    }
                }
            }

            // if we reach here, this means there is no way out.
            Console.WriteLine("Invalid Maze, No Exit.");
        }

        // Check if we need to load the backUp or not.
        private bool ShouldBackup(Vertex currentVertex)
        {
            // To avoid null exception, check if this is not the first element (root).
            if (previous != null)
                // go through all neighbors (v) of previous vertex.
                foreach (Vertex v in previous.getNeighbors())
                {
                    // if we found out that the current vertex was a niegbor of the pervious vertex, this means we didnt backtrack yet, so- set getBackUp to false. 
                    if (String.Equals(v.ToString(), currentVertex.ToString()))
                        return false;
                }
            // if it was not a nieghbor of the previous then we must load the backUp.
            return true;
        }

        // Print all Attributes in the List "path", the Exit is not included in the List and will be Printed separately at the end of ("DFS_SolveMaze") method.
        private void printPath(List<Vertex> path)
        {
            foreach(Vertex v in path)
            {
                Console.Write(v + " -> ");
            }
        }
    }

    class Vertex
    {
        // The name of the Vertex, it is set as the number of the vertex in the numberic order.
        private String name;
        // To check if we have visited the Vertez before.
        private bool Visited;
        // The type is for the maze problem (0, 1, 2, or 3).
        private int type, X, Y;
        // The neighbors of the vertex.
        private List<Vertex> neighbors = new List<Vertex>();

        // Constructor.
        public Vertex(String name)
        {
            this.name = name;
        }

        // Setters and getters.

        // Visited getter
        public bool getVisited()
        {
            return Visited;
        }

        // Visited setter.
        public void setVisited(bool Visited)
        {
            this.Visited = Visited;
        }

        // type getter.
        public int gettype()
        {
            return type;
        }

        // type setter.
        public void settype(int type)
        {
            this.type = type;
        }

        public int getX()
        {
            return X;
        }

        // type setter.
        public void setX(int X)
        {
            this.X = X;
        }

        public int getY()
        {
            return Y;
        }

        // type setter.
        public void setY(int Y)
        {
            this.Y = Y;
        }

        // Neighbors getter
        public List<Vertex> getNeighbors()
        {
            return neighbors;
        }

        // Add new Neighbors.
        public void addNeighbors(Vertex newNeighbor)
        {
            this.neighbors.Add(newNeighbor);
        }

        // when we call the Vertex on a print, it will print what this method returns.
        public override string ToString()
        {
            return name;
        }
    }
}

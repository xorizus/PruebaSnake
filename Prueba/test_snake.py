import unittest
import pygame
from snake import *

class SnakeGameTests(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Snake Game")
        
    def test_initial_state(self):
        self.assertEqual(snake_position, [100, 50])
        self.assertEqual(snake_body, [[100, 50], [90, 50], [80, 50]])
        self.assertTrue(isinstance(fruit_position[0], int))
        self.assertTrue(isinstance(fruit_position[1], int))
        self.assertTrue(isinstance(fruit_spawned, bool))
        self.assertIn(direction, ['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.assertEqual(score, 0)
        
    def test_change_direction(self):
        change_direction('RIGHT')
        self.assertEqual(direction, 'RIGHT')
        change_direction('LEFT')
        self.assertEqual(direction, 'LEFT')
        change_direction('UP')
        self.assertEqual(direction, 'UP')
        change_direction('DOWN')
        self.assertEqual(direction, 'DOWN')
        
    def test_move_snake(self):
        global snake_position, snake_body
        snake_position = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]
        
        move_snake('RIGHT')
        self.assertEqual(snake_position, [110, 50])
        self.assertEqual(snake_body, [[110, 50], [100, 50], [90, 50]])
        
        move_snake('LEFT')
        self.assertEqual(snake_position, [100, 50])
        self.assertEqual(snake_body, [[100, 50], [110, 50], [100, 50]])
        
        move_snake('UP')
        self.assertEqual(snake_position, [100, 40])
        self.assertEqual(snake_body, [[100, 40], [100, 50], [110, 50]])
        
        move_snake('DOWN')
        self.assertEqual(snake_position, [100, 50])
        self.assertEqual(snake_body, [[100, 50], [100, 40], [100, 50]])
        
    def test_check_collision(self):
        global snake_position, snake_body, fruit_position, fruit_spawned, score
        snake_position = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]
        fruit_position = [100, 60]
        fruit_spawned = True
        score = 0
        
        check_collision()
        self.assertEqual(score, 1)
        self.assertFalse(fruit_spawned)
        
        snake_position = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]
        fruit_position = [150, 60]
        fruit_spawned = True
        score = 0
        
        check_collision()
        self.assertEqual(score, 0)
        self.assertTrue(fruit_spawned)
        
    def test_game_over(self):
        with self.assertRaises(SystemExit):
            game_over()
        
if __name__ == '__main__':
    unittest.main()

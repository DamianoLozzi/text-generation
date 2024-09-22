import unittest
from text_generation.text_generation import TextGen

SAMPLE_TEXT = "Bring 1 cup of fresh, clean water to a rolling boil, then pour over 1 tea bag or a tea infuser filled with 1 loose-leaf serving. Steep according to the timing above based on your tea variety. If you prefer a stronger flavor, allow the tea to steep 30 to 60 seconds extra. Stir, then remove the tea bags or infuser. Allow the tea to cool to your desired temperature, then pour over ice. Add sweetener, if desired."

class TestTextGen(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.text_gen = TextGen()
        
    async def test_summarize(self):
        text = SAMPLE_TEXT
        expected_summary = "Boil water"
        
        summary = await self.text_gen.summarize(text)
        
        self.assertTrue(summary.startswith(expected_summary))
        
    async def test_generate_name_filename(self):
        text = SAMPLE_TEXT
        
        name = await self.text_gen.generate_name(text, type='filename')
        
        self.assertTrue(name.startswith("steep_and_cool_tea_a_guide_to_choosing_the_right_flavor"))
        
    async def test_generate_name_title(self):
        text = SAMPLE_TEXT
        expected_name = "Steep and Cool Tea A Guide to Choosing the Right Flavor"
        
        name = await self.text_gen.generate_name(text, type='title')
        
        self.assertEqual(name, expected_name)
        
    async def test_generate_summary(self):
        text = "Bring 1 cup of fresh, clean water to a rolling boil, then pour over 1 tea bag or a tea infuser filled with 1 loose-leaf serving. Steep according to the timing above based on your tea variety. If you prefer a stronger flavor, allow the tea to steep 30 to 60 seconds extra. Stir, then remove the tea bags or infuser. Allow the tea to cool to your desired temperature, then pour over ice. Add sweetener, if desired."
        expected_summary = "This text provides instructions on how to"
        
        summary = await self.text_gen.generate_summary(text)
        
        self.assertTrue(summary.startswith(expected_summary))
        
    async def test_ask_boolean(self):
        text = "Is the Sun big?"
        expected_response = True
        
        response = await self.text_gen.ask_boolean(text)
        
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
from random import choice, randint

def get_response(user_input: str) -> str:
  lowered: str = user_input.lower()

  if lowered == '':
    return 'I am a bot that can help you with your questions. Just ask me anything!'
  elif 'hello' in lowered:
    return 'Halo cantik gemesin!'
  elif 'roll dice' in lowered:
    return f'You rolled a {randint(1, 6)}!'
  else:
    return choice([
      'I am sorry, I do not understand your question.',
      'I am a bot that can help you with your questions. Just ask me anything!',
      'I am not sure what you are asking for.',
      'I am unable to process your request at the moment.',
      'I am not sure what you are asking for.',
      'I am sorry, I do not understand your question.',
      'I am a bot that can help you with your questions. Just ask me anything!',
      'I am not sure what you are asking for.',
      'I am unable to process your request at the moment.',
      'I am not sure what you are asking for.'
    ])
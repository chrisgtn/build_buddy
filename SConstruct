import os


# Read build mode
build_mode = ARGUMENTS.get('BUILD', 'release')

if build_mode == 'debug':
    cflags = ['-Wall', '-g', '-DDEBUG']
else:
    cflags = ['-Wall', '-O2', '-DNDEBUG']

env = Environment(CC='gcc', CFLAGS=cflags)

# Make sure build directory exists
if not os.path.exists('build'):
    os.makedirs('build')

env.Program(target='build/main', source=['src/main.c', 'src/math_utils.c'])

import os

# Read build mode
build_mode = ARGUMENTS.get('BUILD', 'release')

if build_mode == 'debug':
    cflags = ['-Wall', '-g', '-DDEBUG']
else:
    cflags = ['-Wall', '-O2', '-DNDEBUG']

# Setup environment
env = Environment(CC='gcc', CFLAGS=cflags)

# Create build directory if it doesn't exist
if not os.path.exists('build'):
    os.makedirs('build')

# Define source files
sources = ['src/main.c', 'src/sound_utils.c']

# Build target
env.Program(target='build/main', source=sources)

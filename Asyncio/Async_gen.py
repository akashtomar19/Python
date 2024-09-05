
# Don’t get bogged down in generator-based coroutines, which have been deliberately outdated by async/await.
async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y

# Here's why this causes a SyntaxError:

# yield from in Normal Generators: In regular (synchronous) generator functions, yield from is used to delegate part of the generator's operations to another generator. This allows you to yield all values from the delegated generator.


def gen(x):
    for i in range(x):
        yield i

def m(x):
    yield from gen(x)
# This works fine in synchronous code.

# async Functions: When you declare a function with async def, it becomes an asynchronous function, which means you can use await and async for within it. However, yield from is not allowed in async functions because yield from is a feature of synchronous generators.

# Asynchronous Generators: In an async function, if you want to yield values asynchronously, you should use async for to iterate over the values of another asynchronous generator.

# Correcting the Code
# If you want to use an asynchronous generator and delegate to another generator, you should do it like this:


async def gen(x):
    for i in range(x):
        yield i

async def m(x):
    async for value in gen(x):
        yield value
# In this corrected version:

# gen(x) is an asynchronous generator.
# In m(x), you use async for to iterate over the values from gen(x) and yield them.
# This allows the function m(x) to asynchronously yield values, delegating the generation of those values to gen(x).

# Key Points:
# yield from: Used only in synchronous generators.
# async for: Used to iterate over asynchronous generators in async functions.
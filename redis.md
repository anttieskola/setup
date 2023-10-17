# Redis
Redis the great in-memory database with atomic operations.

[Redis](https://github.com/redis/redis)

It is simple to compile and all dependencies should be installed already during [node installation](/installation.md). Just compile it with make/gcc.

My first program only created multiplethreads that appended random character to same key until timeout occured when string size had grown large enough.

Now started testing [Redis.OM](https://github.com/redis/redis-om-dotnet) and noticed that it uses more advanced API as got errors from unknown commands creating index. The index uses `FT... commands and those are defined in separate module called [RediSearch](https://github.com/RediSearch/RediSearch). Also [RedisJSON](https://github.com/RedisJSON/RedisJSON) is needed.

##  Module Python issue
As my OS has nice python setup where only debian packages are possible to install, I created conda environment with Python 3.10 so the python tests can compile without issue.

```bash
conda create --name redis python=3.10

conda activate redis
```

## Compiling RedisJSON
It's rust application so had almost all ready but you can find out third party requirements from the `sbin/setup` scripts.

## Compiling RediSearch
This is c++ application. Has same `sbin/setup` script to set dependencies.c

Here I had to modify one third party Makefile as GCC version 12 has a bug.

- Remove "-Wall" option from deps/VectorSimlarity/src/VecSim/spaces/CMakeLists.txt
- [Issue @ VectorySimilary](https://github.com/RedisAI/VectorSimilarity/issues/414)
- [Issue @ GCC](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105593)

```diff
antti@zeus:/home/projects/RediSearch/deps/VectorSimilarity$ git diff
diff --git a/src/VecSim/spaces/CMakeLists.txt b/src/VecSim/spaces/CMakeLists.txt
index d361cf8..75e4e7d 100644
--- a/src/VecSim/spaces/CMakeLists.txt
+++ b/src/VecSim/spaces/CMakeLists.txt
@@ -42,7 +42,7 @@ if(CMAKE_HOST_SYSTEM_PROCESSOR MATCHES "(x86_64)|(AMD64|amd64)|(^i.86$)")
        endif()
 endif()
 
-set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror -Wall")
+set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror")
 
 # Here we are compiling the space selectors with the relevant optimization flag.
 add_library(VectorSimilaritySpaces
```

# Configuration

```
# default (note, has no protection atm)
bind * -::*

# modules
loadmodule /home/projects/RediSearch/bin/linux-x64-release/search/redisearch.so
loadmodule /home/projects/RedisJSON/target/release/librejson.so

# open to everyone, not good...
protected-mode no
```

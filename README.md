# how to use

```bash
usage: g [options] [param]
example: g -c index.ts" - running command: git checkout index.ts
```

## how to multiple arguments

```bash
# usage
g [options] [params...]

# example
g -amu index.ts "feat: Update index.ts"

# running command
git add index.ts && git commit -m "feat: Update index.ts" && git push
```

## help command

```bash
g -h # show git command help
```

# options

## pull category arguments

```bash
g -f # git fetch
g -c <branch | path> # git checkout <branch | path>
g -p # git fetch && git pull
```

## commit category arguments

```bash
g -a <path> # git add <path>
g -m <commit title> # git commit -m <commit title>
g -u # git push
```

## show category arguments

```bash
g -d # git diff <path | none>
g -s # git status <path | none>
```

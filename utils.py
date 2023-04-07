from typing import Iterator, Generator


def slice_limit(it: Iterator, limit: int) -> Generator:
    i = 0
    for item in it:
        if i < limit:
            yield item
        else:
            break
        i += 1


def make_query_response(cmd, val, it: Iterator) -> Iterator | Generator:
    match cmd:
        case "filter":
            return filter(lambda x: val in x, it)
        case "map":
            return map(lambda v: v.split(" ")[int(val)], it)
        case "unique":
            return iter(set(it))
        case "sort":
            return iter(sorted(it, reverse=val == 'desc'))
        case "limit":
            return slice_limit(it, int(val))

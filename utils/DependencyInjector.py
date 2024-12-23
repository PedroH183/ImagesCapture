from utils.Singleton import SingletonInterface

class DependencyInjector:
    """
        Dependency Injector class to resolve dependencies
    """

    _providers = {}
    __metaclass__ = SingletonInterface

    @classmethod
    def add_provider(cls, key, provider): 
        cls._providers[key] = provider

    @classmethod
    def resolve(cls, key: str):
        provider = cls._providers.get(key, "")

        if not provider:
            raise Exception(f"Provider not found for key {key}, provider state :: {cls._providers}")

        return provider()

    @classmethod
    def inject(cls, *dependencies):
        def decorator(func):
            def wrapper(*args, **kwargs):
                resolved_deps = {dep: cls.resolve(dep) for dep in dependencies}
                kwargs.update(resolved_deps)
                return func(*args, **kwargs)
            return wrapper
        return decorator
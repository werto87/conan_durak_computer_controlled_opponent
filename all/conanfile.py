from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get


class DurakComputerControlledOpponent(ConanFile):
    name = "durak_computer_controlled_opponent"
    homepage = "https://github.com/werto87/durak_computer_controlled_opponent"
    description = "Create a lookup table for durak"
    topics = ("computer_controlled_opponent")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "CMakeDeps", "CMakeToolchain"


    def configure(self):
        self.options["boost"].header_only = True
        self.options["small_memory_tree"].with_st_tree = True

    def requirements(self):
        self.requires("boost/1.85.0",force=True)
        self.requires("durak/1.0.5",transitive_headers=True)
        self.requires("st_tree/1.2.1")
        self.requires("small_memory_tree/5.2.0",transitive_headers=True)
        self.requires("stlplus/3.16.0")
        self.requires("confu_soci/0.3.21")
        self.requires("magic_enum/[>=0.9.5 <10]")


    def source(self):
        get(self, **self.conan_data["sources"][self.version],strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self, src_folder=self.name+"-"+str(self.version))

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [self.name]
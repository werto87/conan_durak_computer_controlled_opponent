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
        self.options["soci"].with_boost = True
        self.options["soci"].with_sqlite3 = True

    def requirements(self):
        self.requires("durak/1.0.3", transitive_libs=True, transitive_headers=True)
        self.requires("st_tree/1.2.1")
        self.requires("boost/1.84.0", force=True)
        self.requires("small_memory_tree/4.0.2", transitive_libs=True, transitive_headers=True)
        self.requires("range-v3/0.12.0")
        self.requires("confu_soci/0.3.20")


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
package com.example.caraoucoroa

import android.content.Intent
import android.os.Bundle
import android.widget.ImageButton
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    var btnJogar : ImageButton? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        mainConfig()
        listeners()

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
    }

    fun mainConfig() {
        btnJogar = findViewById<ImageButton>(R.id.imgBtnJogar)
    }

    fun listeners() {
        btnJogar?.setOnClickListener() {
            val intent = Intent(this, MoedaActivity::class.java)
            intent.putExtra("sorteado", Random.nextInt(2))
            startActivity(intent)
        }
    }

}
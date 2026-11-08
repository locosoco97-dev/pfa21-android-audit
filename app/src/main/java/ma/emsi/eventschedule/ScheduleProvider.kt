package ma.emsi.eventschedule

// Squelette pedagogique : aucun comportement requis pour l'audit statique du manifeste.
class ScheduleProvider : android.content.ContentProvider() {
    override fun onCreate() = true
    override fun query(u: android.net.Uri, p: Array<String>?, s: String?, a: Array<String>?, o: String?) = null
    override fun getType(u: android.net.Uri) = null
    override fun insert(u: android.net.Uri, v: android.content.ContentValues?) = null
    override fun delete(u: android.net.Uri, s: String?, a: Array<String>?) = 0
    override fun update(u: android.net.Uri, v: android.content.ContentValues?, s: String?, a: Array<String>?) = 0
}
